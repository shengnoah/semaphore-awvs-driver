#-*- coding:utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from sidecar.models import cmdb,testcase
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

            max_id = testcase.objects.all().order_by("-id")[0]
            print "##########################"
            print type(max_id)
            print max_id.id
            print "##########################"
            new_maxid = max_id.id + 1
            print(new_maxid)
            testcase.objects.create(id=(max_id.id + 1),name1="a", name2="b", name3="c")
 
            self.stdout.write(self.style.SUCCESS(u'命令%s执行成功, 参数为%s' % (__file__, options['index'])))
        except Exception, ex:
            self.stdout.write(self.style.ERROR(u'命令执行出错'))
            print ex
