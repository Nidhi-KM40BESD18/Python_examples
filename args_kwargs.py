def func_args(name, *args, **kwargs):
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(f'key {k} has {v} value')

stu = ['nisha', 'misha', 'ani', 'harry', 'vicky']

dic = {'name1':'nidhi', 'sname':'chauhan', 'age':20}
func_args('nicky', *stu, **dic)



