'''
14-2 Josephus排列 约瑟夫环 sohu's shame
a. m constant → n
b. m not constant → nlgn by ost
'''
from practice.autumn.rbtreesubcnt import RBTree as ost

class Solution:
    def josephus_n(self,n,m):
        num = [i for i in range(1,n+1)]
        josephus = []
        cnt = 0
        i = 0
        while len(josephus) < n:
            if num[i] != 0:
                cnt += 1
            if cnt == m:
                josephus.append(num[i])
                num[i] = 0
                cnt = 0
            i = (i+1) % n
        return josephus

    def josephus_nlgn(self,n,m):
        tree = ost()
        josephus = []
        for i in range(1,n+1):
            tree.rb_insert(i)
        tree.level_travelsal()
        p = tree.search(1);
        while tree.root != tree.nil:
            d = tree.os_rank_successor_node_loop(p,m-1)
            josephus.append(d.key)
            p = tree.os_rank_successor_node_loop(d,1)
            tree.rb_delete_node(d)
        return josephus

if __name__ == '__main__':
    slt = Solution()
    rn = slt.josephus_n(17,13)
    print(rn)
    rnlgn = slt.josephus_nlgn(17,13)
    print(rnlgn)