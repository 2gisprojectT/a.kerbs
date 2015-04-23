__author__ = 'Sasha'

class Lion:
    error = ""
    def __init__(self, state, table_state):

        if state == "":
            raise Exception('Empty state')

        if table_state == "":
            raise Exception('Empty table state')

        self.error = None
        s = list(table_state.keys())
        s = list(set(e[0] for e in s))
        if not (state in s):
           raise Exception('status is not in the table state: ' + state)
        #for i in s:
        #    if state == i[0]:
        #        self.error = 'State in Table State'
        #if self.error == None:
        #    Exception('status is not in the table state: ' + state)

        self.action = ""
        self.state = state
        self.table_state = table_state


    def isAction(self, in_object):
        if in_object == "":
            raise Exception("Empty in_object")
        if(self.state, in_object) not in self.table_state:
            raise Exception('not in_object in table state: ' + in_object)
        self.action = self.table_state[(self.state, in_object)][1]
        self.state = self.table_state[(self.state, in_object)][0]





if __name__ == '__main__':

    table = {
        ("hungry", "antelope"): ("fed", "eat"),
        ("hungry", "hunter"): ("hungry", "run"),
        ("hungry", "tree"): ("hungry", "sleep"),
        ("fed", "antelope"): ("hungry", "sleep"),
        ("fed", "hunter"): ("hungry", "run"),
        ("fed", "tree"): ("hungry", "see")
    }

    status = 'hungry'
    L = Lion(status, table)
    print('Choose objects: antelope, hunter, tree')
    print('If you want quit,print exit')
    while 1:
        print('Now lion is ' + L.state)
        try:
            obj = input().lower()
            if obj == 'exit':
                break
            L.isAction(obj)
            print('Lion  '+L.action)
        except:
            print('Error, lion don\'t know object and action for him')

