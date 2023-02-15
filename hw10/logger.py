
def logger(id, input, output):
    with open('botLog.txt', 'a') as data:
        data.write(f'{id}  {input} = {output} \n')











