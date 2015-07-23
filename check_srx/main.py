""" Check SRX Cluster status """
import nagiosplugin
import argparse
import logging

from jnpr.junos import Device

_log = logging.getLogger('nagiosplugin')

from check_srx.tables.chassis_cluster_status import ChassisClusterStatus

class ClusterStatus(nagiosplugin.Resource):
    def __init__(self, dev):
        self.dev = dev

    def probe(self):
        ccs = ChassisClusterStatus(self.dev)
        ccs.get()
        for redundancy_group in ccs:
            for device_nr in (0, 1):
                _log.debug("RG {} device {} ({}) state {}".format(
                    redundancy_group['group_id'],
                    device_nr,
                    redundancy_group['device{}_name'.format(device_nr)],
                    redundancy_group['device{}_status'.format(device_nr)]))

                m_name = 'rg_{}_device{}_status'.format(
                    redundancy_group['group_id'], device_nr),
                m = nagiosplugin.Metric(
                    m_name,
                    redundancy_group['device{}_status'.format(device_nr)],
                    context='cluster_node_status')
                yield m


class NodeStatusContext(nagiosplugin.context.Context):
    def evaluate(self, metric, resource):
        if metric.value in ['primary', 'secondary']:
            return self.result_cls(nagiosplugin.state.Ok, None, metric)
        return self.result_cls(nagiosplugin.state.Critical,
                               'Wrong node status: {}'.format(metric), metric)


class NodeStatusSummary(nagiosplugin.Summary):
    def ok(self, results):
        return ' '.join(x.metric.description for x in results)


@nagiosplugin.guarded
def main():
    argp = argparse.ArgumentParser(description=__doc__)
    argp.add_argument('-H', '--hostname', metavar='HOSTNAME',
                      help='SRX hostname or IP address')
    argp.add_argument('-u', '--username', metavar='USER',
                      help='User name')
    argp.add_argument('-v', '--verbose', action='count', default=0,
                      help='increase output verbosity (use up to 3 times)')

    args = argp.parse_args()
    if args.hostname is None:
        raise nagiosplugin.CheckError('No hostname given')
    dev = Device(host=args.hostname, user=args.username)
    dev.open()
    check = nagiosplugin.Check(
        ClusterStatus(dev),
        NodeStatusContext(
            'cluster_node_status',
            fmt_metric='{name[0]}: {value}'),
        NodeStatusSummary()
    )
    check.main(verbose=args.verbose)

if __name__ == '__main__':
    main()
