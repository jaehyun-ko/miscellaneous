import time


def elapsed(f):
    def wrap(*args):
        start_r = time.perf_counter()
        start_p = time.process_time()
        # �Լ� ����
        ret = f(*args)
        end_r = time.perf_counter()
        end_p = time.process_time()
        elapsed_r = end_r - start_r
        elapsed_p = end_p - start_p

        print(f'{f.__name__} elapsed: {elapsed_r:.6f}sec (real) / {elapsed_p:.6f}sec (cpu)')
        return ret
   # �Լ� ��ü�� return
    return wrap



@elapsed
def comp_flat(l):
    return [item for sublist in m for item in sublist]

@elapsed
def sum_flat(l):
    return sum(l,[])

    
if __name__ == "__main__":
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    
    sum_flat(m)
    comp_flat(m)