import unittest2 as unittest
from zope.interface import implements

from plonesocial.microblog.interfaces import IStatusContainer
from plonesocial.microblog.interfaces import IStatusUpdate
from plonesocial.microblog import statuscontainer
from plonesocial.microblog import statusupdate


class StatusContainer(statuscontainer.BaseStatusContainer):
    """Override actual implementation with unittest features"""

    implements(IStatusContainer)

    def _check_permission(self, perm="read"):
        pass


class StatusUpdate(statusupdate.StatusUpdate):
    """Override actual implementation with unittest features"""

    implements(IStatusUpdate)

    def __init__(self, text, userid, creator=None, thread=None):
        statusupdate.StatusUpdate.__init__(self, text)
        self.userid = userid
        if creator:
            self.creator = creator
        else:
            self.creator = userid

        if thread:
            self.thread = thread

    def _init_userid(self):
        pass

    def _init_creator(self):
        pass

    def _init_thread(self):
        pass


class TestStatusContainer_Tags(unittest.TestCase):

    ## user/tag accessors

    def test_keys(self):
        container = StatusContainer()
        # add normal status update
        status = StatusUpdate('test', 'arnold')
        container.add(status)
        (key, value) = list(container.items())[0]
        self.assertEqual(key, value.id)
        self.assertEqual(status, value)
        # add reply to status.id
        sa = StatusUpdate('test reply a', 'arnold', thread=status.id)
        container.add(sa)
        sb = StatusUpdate('test reply b', 'bernard', thread=status.id)
        container.add(sb)
        sc = StatusUpdate('test reply c', 'cary', thread=status.id)
        container.add(sc)
        # get all thread items from parent status.id
        keys = [x for x in container.thread_keys(thread=status.id)]
        self.assertEqual([sc.id, sb.id, sa.id], keys)

    def test_values(self):
        container = StatusContainer()
        # add normal status update
        status = StatusUpdate('test', 'arnold')
        container.add(status)
        (key, value) = list(container.items())[0]
        self.assertEqual(key, value.id)
        self.assertEqual(status, value)
        # add reply to status.id
        sa = StatusUpdate('test reply a', 'arnold', thread=status.id)
        container.add(sa)
        sb = StatusUpdate('test reply b', 'bernard', thread=status.id)
        container.add(sb)
        sc = StatusUpdate('test reply c', 'cary', thread=status.id)
        container.add(sc)
        # get all thread items from parent status.id
        values = [x for x in container.thread_values(thread=status.id)]
        self.assertEqual([sc, sb, sa], values)

    def test_items(self):
        container = StatusContainer()
        # add normal status update
        status = StatusUpdate('test', 'arnold')
        container.add(status)
        (key, value) = list(container.items())[0]
        self.assertEqual(key, value.id)
        self.assertEqual(status, value)
        # add reply to status.id
        sa = StatusUpdate('test reply a', 'arnold', thread=status.id)
        container.add(sa)
        sb = StatusUpdate('test reply b', 'bernard', thread=status.id)
        container.add(sb)
        sc = StatusUpdate('test reply c', 'cary', thread=status.id)
        container.add(sc)
        # get all thread items from parent status.id
        values = [x[1] for x in container.thread_items(thread=status.id)]
        self.assertEqual([sc, sb, sa], values)

    def test_get_thread_by_thread_item(self):
        container = StatusContainer()
        # add normal status update
        status = StatusUpdate('test', 'arnold')
        container.add(status)
        (key, value) = list(container.items())[0]
        self.assertEqual(key, value.id)
        self.assertEqual(status, value)
        # add reply to status.id
        sa = StatusUpdate('test reply a', 'arnold', thread=status.id)
        container.add(sa)
        sb = StatusUpdate('test reply b', 'bernard', thread=status.id)
        container.add(sb)
        sc = StatusUpdate('test reply c', 'cary', thread=status.id)
        container.add(sc)
        # get all thread items from thread item sa.id
        si = container.get(sa.id)
        if getattr(si, 'thread'):
            values = [x[1] for x in container.thread_items(thread=si.thread)]
            self.assertEqual([sc, sb, sa], values)

    def test_get_nothing_by_none_thread_item(self):
        container = StatusContainer()
        # add normal status update
        status = StatusUpdate('test', 'arnold')
        container.add(status)
        (key, value) = list(container.items())[0]
        self.assertEqual(key, value.id)
        self.assertEqual(status, value)
        # add reply to status.id
        sa = StatusUpdate('test reply a', 'arnold', thread=status.id)
        container.add(sa)
        sb = StatusUpdate('test reply b', 'bernard', thread=status.id)
        container.add(sb)
        sc = StatusUpdate('test reply c', 'cary', thread=status.id)
        container.add(sc)
        # test by giving none
        values = [x[1] for x in container.thread_items(thread=None)]
        self.assertEqual([], values)

    #def test_user_keys_match(self):
    #    container = StatusContainer()
    #    sa = StatusUpdate('test a', 'arnold')
    #    container.add(sa)
    #    sb = StatusUpdate('test b', 'bernard')
    #    container.add(sb)
    #    sc = StatusUpdate('test c', 'cary')
    #    container.add(sc)
    #    keys = [x for x in container.user_keys(['arnold', 'bernard', 'cary'],
    #                                           tag='b')]
    #    self.assertEqual([sb.id], keys)
    #
    #def test_user_keys_nomatch(self):
    #    container = StatusContainer()
    #    sa = StatusUpdate('test a', 'arnold')
    #    container.add(sa)
    #    sb = StatusUpdate('test b', 'bernard')
    #    container.add(sb)
    #    sc = StatusUpdate('test c', 'cary')
    #    container.add(sc)
    #    keys = [x for x in container.user_keys(['arnold', 'bernard'],
    #                                           tag='c')]
    #    self.assertEqual([], keys)
    #
    #def test_user_values(self):
    #    container = StatusContainer()
    #    sa = StatusUpdate('test a', 'arnold')
    #    container.add(sa)
    #    sb = StatusUpdate('test b', 'bernard')
    #    container.add(sb)
    #    sc = StatusUpdate('test c', 'cary')
    #    container.add(sc)
    #    values = [x for x in
    #              container.user_values(['arnold', 'bernard', 'cary'],
    #                                    tag='b')]
    #    self.assertEqual([sb], values)
    #
    #def test_user_items(self):
    #    container = StatusContainer()
    #    sa = StatusUpdate('test a', 'arnold')
    #    container.add(sa)
    #    sb = StatusUpdate('test b', 'bernard')
    #    container.add(sb)
    #    sc = StatusUpdate('test c', 'cary')
    #    container.add(sc)
    #    values = [x[1] for x in
    #              container.user_items(['arnold', 'bernard', 'cary'],
    #                                   tag='b')]
    #    self.assertEqual([sb], values)
    #
    #def test_keys_nosuchtag(self):
    #    container = StatusContainer()
    #    sa = StatusUpdate('test a', 'arnold')
    #    container.add(sa)
    #    sb = StatusUpdate('test b', 'bernard')
    #    container.add(sb)
    #    sc = StatusUpdate('test c', 'cary')
    #    container.add(sc)
    #    keys = [x for x in container.keys(tag='foo')]
    #    self.assertEqual([], keys)
    #
    #def test_user_keys_nosuchtag(self):
    #    container = StatusContainer()
    #    sa = StatusUpdate('test a', 'arnold')
    #    container.add(sa)
    #    sb = StatusUpdate('test b', 'bernard')
    #    container.add(sb)
    #    sc = StatusUpdate('test c', 'cary')
    #    container.add(sc)
    #    keys = [x for x in container.user_keys(['arnold', 'bernard', 'cary'],
    #                                           tag='foobar')]
    #    self.assertEqual([], keys)
