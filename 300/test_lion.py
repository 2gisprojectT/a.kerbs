from unittest import TestCase
from lion import Lion
import unittest

class Test_Lion(TestCase):

    def setUp(self):
        self.state_In = "test_state_In"
        self.state_Out = "test_state_Out"
        self.action = "test_action"
        self.object = "test_object"
        self.table = {(self.state_In, self.object):(self.state_Out, self.action)}

    def test_init(self):
        self.lion = Lion(self.state_In, self.table)
        self.assertEqual(self.state_In, self.lion.state, 'State_In have wrong value')
        self.assertEqual(self.table, self.lion.table_state, 'table_state have wrong value')

    def test_init_exception_status(self):
        self.assertRaises(Exception, Lion.__init__, "", self.table )

    def test_init_exception_table(self):
        self.assertRaises(Exception, Lion.__init__, self.state_In, "" )

    def test_init_exception_status_in_table(self):
        self.assertRaises(Exception, Lion.__init__, "Error_State", self.table )

    def test_action(self):

        self.lion = Lion(self.state_In, self.table)
        self.lion.isAction("test_object")
        self.assertEqual(self.state_Out, self.lion.state, 'State_Out have wrong value')
        self.assertEqual(self.action, self.lion.action, 'Action have wrong value')

    def test_action_exception_object(self):
        self.lion = Lion(self.state_In, self.table)
        self.assertRaises(Exception, Lion.isAction, '' )

    def test_action_exception_object_in_table(self):
        self.lion = Lion(self.state_In, self.table)
        self.assertRaises(Exception, Lion.isAction, 'Error_Object' )

if __name__ == '__main__':
    unittest.main()
