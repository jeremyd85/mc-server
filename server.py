import argparse
import dropbox


def backup(args):
    name = args.name
    if name is not None:
        pass

def restore(args):
    pass

def stop(args):
    pass

def restart(args):
    pass

def start(args):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Script manages Minecraft Server')
    subparsers = parser.add_subparsers(help='Commands useful for managing Minecraft Server')
    
    parser_backup = subparsers.add_parser('backup')
    parser_backup.add_argument('--name', type=str, help='Name the backup for easy restore later on')
    parser_backup.set_defaults(func=backup)

    parser_restore = subparsers.add_parser('restore')
    parser_restore.add_argument('--time', help='Time of safe state')
    parser_restore.add_argument('--name', help='Convenience name that can be used on restore')
    parser_restore.set_defaults(func=restore)

    parser_stop = subparsers.add_parser('stop')
    parser_stop.set_defaults(func=stop)

    parser_restart = subparsers.add_parser('restart')
    parser_restart.set_defaults(func=restart)

    parser_start = subparsers.add_parser('start')
    parser_start.set_defaults(func=start)

    args = parser.parse_args()
    args.func(args)