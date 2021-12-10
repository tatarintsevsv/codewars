# https://www.codewars.com/kata/51fda2d95d6efda45e00004e
class User:
    rank = -8
    progress = 0
    def inc_progress(self,x):
        if x not in range(-8,9) or x==0:
            raise TextError('unsupported progress value')
            return
        if x > 0:
            x -= 1
        rank = self.rank if self.rank < 0 else self.rank-1
        delta = x-rank
        dp = 0
        if delta == 0:
            dp = 3
        if delta == -1:
            dp = 1
        if delta > 0:
            dp = delta*delta*10
        self.progress +=dp
        while self.progress>=100:
            self.progress-=100
            rank+=1
        self.rank = rank if rank < 0 else min(8,rank+1)
        if self.rank==8:
            self.progress=0
