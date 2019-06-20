#-*- coding:utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
import traceback
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-i',
            '--index',
            action='store',
            dest='index',
            default='close',
            help='name of author.',
        )
        parser.add_argument(
            '-f',
            '--file',
            action='store',
            dest='file',
            default='open',
            help='name of author.',
        )

    def handle(self, *args, **options):
        try:
            if options['index']:
                print 'hello world, %s' % options['index']
            if options['file']:
                print 'input file, %s' % options['file']

            from jsonrpc.proxy import ServiceProxy
            s = ServiceProxy('http://localhost:5000/json/') 
            s.myapp.sayHello('Sam')
            
            self.stdout.write(self.style.SUCCESS(u'命令%s执行成功, 参数为%s' % (__file__, options['index'])))
        except Exception, ex:
            traceback.print_exc()
            self.stdout.write(self.style.ERROR(u'命令执行出错'))
