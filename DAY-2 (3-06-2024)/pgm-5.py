'''Take a string input which has only two characters M & F which represents Male and Female.
    The output should be 0 when count(Male)=count(Female), M when Male>Female or F when Female>Male'''
a=input()
if (a.count('M') or a.count('m'))==(a.count('F')or a.count('f')):
    print('0')
elif (a.count('M') or a.count('m'))>(a.count('F')or a.count('f')):
    print('M')
elif (a.count('M') or a.count('m'))<(a.count('F')or a.count('f')):
    print('F')   