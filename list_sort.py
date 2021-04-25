class Node():
    """ノードクラス

    双方向連結リストクラスDoublyLinkedList()のノードオブジェクトとして利用する

    Attributes:
        data(free) : ノードのデータ
        prev(obj) : 対象ノードの前ノード
        next(obj) : 対象ノードの次ノード
    """

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList():
    """双方向連結リストクラス

    双方向連結リストクラス
    データの挿入削除及び3種類のソート(バブルソート、選択ソート、挿入ソート)メソッドを持つ
    """

    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert(self, x):
        """挿入メソッド

         連結リストの先頭にキーxを持つ要素を継ぎ足す

        Args:
            x(free): 挿入するデータ

        Examples:
            >>> dll = DoublyLinkedList()
            >>> dll.insert(3)
            >>> dll.insert(7)
            >>> dll.show()
            7 3
        """
        new_node = Node(x, None, None)
        # それまでにnodeが一個もない場合(初めての追加)
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        # すでにnodeがある場合
        else:
            new_node.next = self.head_node
            self.head_node.prev = new_node
            self.head_node = new_node

    def insert_list_as_dll(self, lst):
        """挿入メソッド

         リストの要素を同じ順番になるように双方向連結リストの先頭に追加する

        Args:
            lst(list): 挿入するデータのリスト

        Examples:
            >>> dll = DoublyLinkedList()
            >>> dll.insert_list_as_dll([1,2,3,4,5])
            >>> dll.show()
            1 2 3 4 5
        """
        n = len(lst)
        for i in range(n):
            self.insert(lst[n-i-1])

    def delete(self, x):
        """指定要素の削除メソッド

        キーxを持つ最初の要素を連結リストから削除する。
        そのような要素が存在しない場合は何もしない。

        Args:
            x(free): 削除するデータ

        Examples:
            >>> dll = DoublyLinkedList()
            >>> dll.insert(3)
            >>> dll.insert(7)
            >>> dll.insert(9)
            >>> dll.delete(7)
            >>> dll.show()
            9 3
        """
        if self.head_node.data == x:
            self.deleteFirst()
        else:
            # データ数が1個でない場合のみ次を調べる
            if self.head_node != self.tail_node:
                checking = self.head_node.next
                while True:
                    # 最後のノードの場合
                    if checking == self.tail_node:
                        if checking.data == x:
                            self.deleteLast()
                            break
                        else:
                            break
                    # 中間ノードの場合
                    else:
                        if checking.data == x:
                            prev_checking = checking.prev
                            next_checking = checking.next
                            prev_checking.next = next_checking
                            next_checking.prev = prev_checking
                            break
                        else:
                            checking = checking.next

    def deleteFirst(self):
        """先頭要素の削除メソッド

        リストの先頭の要素を削除する。

        Examples:
            >>> dll = DoublyLinkedList()
            >>> dll.insert(3)
            >>> dll.insert(7)
            >>> dll.insert(9)
            >>> dll.deleteFirst()
            >>> dll.show()
            7 3
        """
        # 要素が一つの場合
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
        # 要素が複数の場合
        else:
            new_head = self.head_node.next
            new_head.prev = None
            self.head_node = new_head

    def deleteLast(self):
        """末尾要素の削除メソッド

        リストの末尾の要素を削除する。

        Examples:
            >>> dll = DoublyLinkedList()
            >>> dll.insert(3)
            >>> dll.insert(7)
            >>> dll.insert(9)
            >>> dll.deleteLast()
            >>> dll.show()
            9 7
        """
        # 要素が一つの場合
        if self.head_node == self.tail_node:
            self.head_node = None
            self.tail_node = None
        # 要素が複数の場合
        else:
            new_tail = self.tail_node.prev
            new_tail.next = None
            self.tail_node = new_tail

    def show(self):
        """表示用メソッド

        リストの全データをスペースを開けて表示する

        Examples:
            >>> dll = DoublyLinkedList()
            >>> dll.insert(3)
            >>> dll.insert(7)
            >>> dll.insert(9)
            >>> dll.show()
            9 7 3
        """
        if self.head_node is None:
            pass
        else:
            printing = self.head_node
            print(printing.data, end=' ')
            # ノードが1つでない場合
            if self.head_node != self.tail_node:
                printing = self.head_node.next
                while(1):
                    if printing == self.tail_node:
                        print(printing.data)
                        break
                    else:
                        print(printing.data, end=' ')
                        printing = printing.next

    def swap_linked_nodes(self, node1, node2):
        """連結ノードの入れ替えメソッド

         連結した2つのノードの順番を入れ替える

        Args:
            node1(obj): 入れ替える2ノードのうち、前方にあるノード
            node2(obj): 入れ替える2ノードのうち、後方にあるノード
        """
        node0 = node1.prev
        node3 = node2.next

        # node2がtailの場合
        if node3 is None:
            node0.next = node2
            node2.prev = node0
            node1.prev = node2
            node1.next = node3
            node2.next = node1
            self.tail_node = node1
                        
        # node1がheadの場合
        elif node0 is None:
            node2.prev = node0
            node1.prev = node2
            node1.next = node3
            node3.prev = node1
            node2.next = node1
            self.head_node = node2

        else:
            node0.next = node2
            node2.prev = node0
            node1.prev = node2
            node1.next = node3
            node3.prev = node1
            node2.next = node1
        
    def swap_nonlinked_nodes(self, node1, node4):
        """非連結ノードの入れ替えメソッド

         連結していない2つのノードの順番を入れ替える

        Args:
            node1(obj): 入れ替える2ノードのうち、前方にあるノード
            node4(obj): 入れ替える2ノードのうち、後方にあるノード
        """
        node0 = node1.prev
        node2 = node1.next
        node3 = node4.prev
        node5 = node4.next

        # node1が先頭ノード
        if node0 is None:
            #先頭と末尾を入れ替える場合
            if node5 is None:
                node4.prev = node0
                node1.prev = node3
                node1.next = node5
                node4.next = node2
                node3.next = node1
                node2.prev = node4
                self.head_node = node4  
                self.tail_node = node1

            else:
                node4.prev = node0
                node1.prev = node3
                node1.next = node5
                node5.prev = node1
                node4.next = node2
                node3.next = node1
                node2.prev = node4
                self.head_node = node4                          

        elif node5 is None:
            node0.next = node4
            node4.prev = node0
            node1.prev = node3
            node1.next = node5
            node4.next = node2
            node3.next = node1
            node2.prev = node4
            self.tail_node = node1

        else:
            node0.next = node4
            node4.prev = node0
            node1.prev = node3
            node1.next = node5
            node5.prev = node1
            node4.next = node2
            node3.next = node1
            node2.prev = node4

    def insertion_sort(self, comp_func):
        """挿入ソート

        リストの要素を挿入ソートにより並び替える
        並び替えの順序は引数comp_funcにより、
        ・昇順
        ・降順
        ・奇数>偶数かつ奇数内および偶数内では昇順
        から指定できる。

        Args:
            comp_func(ラムダ式): リストの並び替えの仕方を指定する関数
                                ・昇順(comp_func = lambda x, y: x <= y)
                                ・降順comp_func = lambda x, y: x >= y)
                                ・奇数>偶数かつ奇数内および偶数内では昇順
                                  (comp_func = lambda x, y: x <= y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))

        Examples:
            >>> ins = DoublyLinkedList()
            >>> ins.insert_list_as_dll([2, 1, 7, 6])
            >>> ins.insertion_sort(comp_func = lambda x, y: x <= y)
            insertion sort
            1 2 6 7
            >>> ins.insertion_sort(comp_func = lambda x, y: x >= y)
            insertion sort
            7 6 2 1
            >>> ins.insertion_sort(comp_func = lambda x, y: x <= y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
            insertion sort
            1 7 2 6
        """
        print('insertion sort')
        v = self.head_node.next
        while True:
            insert_flag = 0
            if v is None:
                break
            
            insert_point = v.prev
            next_ins_point = insert_point
            # 挿入箇所を調べる
            while True:
                if (insert_point is None) or comp_func(insert_point.data, v.data):
                    insert_point = next_ins_point
                    break
                else:
                    insert_flag = 1
                    next_ins_point = insert_point
                    insert_point = insert_point.prev

            next_v = v.next

            # 先頭もしくは末尾の場合
            if insert_flag == 1:
                node0 = insert_point.prev
                node1 = v.prev
                node2 = v.next

                # 挿入して先頭に来る場合
                if insert_point == self.head_node:
                    #末尾ノードが先頭に来る場合
                    if node2 is None:
                        v.prev = node0
                        insert_point.prev = v
                        v.next = insert_point
                        node1.next = node2             
                        self.head_node = v
                        self.tail_node = node1

                    else:
                        v.prev = node0
                        insert_point.prev = v
                        v.next = insert_point
                        node1.next = node2
                        node2.prev = node1               
                        self.head_node = v

                # 末尾のノードを動かす場合
                elif node2 is None:
                    node0.next = v
                    v.prev = node0
                    insert_point.prev = v
                    v.next = insert_point
                    node1.next = node2
                    self.tail_node = node1

                else:
                    node0.next = v
                    v.prev = node0
                    insert_point.prev = v
                    v.next = insert_point
                    node1.next = node2
                    node2.prev = node1

            v = next_v
        self.show()
        
    def bubble_sort(self, comp_func):
        """バブルソート

        リストの要素をバブルソートにより並び替える
        並び替えの順序は引数comp_funcにより、
        ・昇順
        ・降順
        ・奇数>偶数かつ奇数内および偶数内では昇順
        から指定できる。
    
        Args:
            comp_func(ラムダ式): リストの並び替えの仕方を指定する関数
                                ・昇順(comp_func = lambda x, y: x < y)
                                ・降順comp_func = lambda x, y: x > y)
                                ・奇数>偶数かつ奇数内および偶数内では昇順
                                  (comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))

        Examples:
            >>> ins = DoublyLinkedList()
            >>> ins.insert_list_as_dll([2, 1, 7, 6])
            >>> ins.bubble_sort(comp_func = lambda x, y: x < y)
            bubble sort
            1 2 6 7
            >>> ins.bubble_sort(comp_func = lambda x, y: x > y)
            bubble sort
            7 6 2 1
            >>> ins.bubble_sort(comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
            bubble sort
            1 7 2 6
        """
        print('bubble sort')
        flag = 1
        while (flag == 1):
            flag = 0
            # node1 -> node2の順
            node2 = self.tail_node
            node1 = node2.prev
            while True:
                # nodeが1個もしくはnode2が先頭の場合
                if node1 is None:
                    break

                elif comp_func(node2.data, node1.data):
                    node0 = node1.prev
                    self.swap_linked_nodes(node1, node2)
                    flag = 1
                    node1 = node0
                
                else:
                    node2 = node1
                    node1 = node1.prev
        self.show()
        
    def selection_sort(self, comp_func):
        """選択ソート

        リストの要素を選択ソートにより並び替える
        並び替えの順序は引数comp_funcにより、
        ・昇順
        ・降順
        ・奇数>偶数かつ奇数内および偶数内では昇順
        から指定できる。
        挿入ソートの各計算ステップでの途中結果を1行ずつ表示する。

        Args:
            comp_func(ラムダ式): リストの並び替えの仕方を指定する関数
                                ・昇順(comp_func = lambda x, y: x < y)
                                ・降順comp_func = lambda x, y: x > y)
                                ・奇数>偶数かつ奇数内および偶数内では昇順
                                  (comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))

        Examples:
            >>> ins = DoublyLinkedList()
            >>> ins.insert_list_as_dll([2, 1, 7, 6])
            >>> ins.selection_sort(comp_func = lambda x, y: x < y)
            selection sort
            1 2 6 7
            >>> ins.selection_sort(comp_func = lambda x, y: x > y)
            selection sort
            7 6 2 1
            >>> ins.selection_sort(comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
            selection sort
            1 7 2 6
        """
        print('selection sort')
        target = self.head_node
        while True:
            minj = target
            j = target
            while True:
                if comp_func(j.data, minj.data):
                    minj = j
                if j == self.tail_node:
                    break
                j = j.next
            
            # 入れ替えが必要ない場合
            if target == minj:
                next_target = target.next
            # 隣り合うものを入れ替える場合
            elif target.next == minj:
                next_target = target
                self.swap_linked_nodes(target, minj)
            # 隣り合わないものを入れ替え   
            else:
                next_target = target.next
                self.swap_nonlinked_nodes(target, minj)
            target = next_target
            
            if target == self.tail_node:
                break
        self.show()
              

class DoublyLinkedList_for_card(DoublyLinkedList):
    """双方向連結リストクラス(トランプ用)

    トランプ用の双方向連結リストクラス(1番目の要素が文字、2番目の要素が数字(例: ['D', 3])のリストとしてデータを格納する)
    データの挿入削除及び2種類のソート(バブルソート、選択ソート)、ソートの安定性を調べる
    メソッドを持つ
    """

    def __init__(self):
        super().__init__()
        self.head_node = None
        self.tail_node = None

    def show_trump(self):
        """トランプ表示用メソッド

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        双方向連結リストの全データについて、1番目と2番目の要素をつなげて(例: D3)スペースを開けて表示する。

        Examples:
            >>> ins = DoublyLinkedList_for_card()
            >>> ins.insert(['C', 3])
            >>> ins.insert(['D', 2])
            >>> ins.insert(['S', 4])
            >>> ins.show_trump()
            S4 D2 C3
        """
        if self.head_node is None:
            pass
        else:
            printing = self.head_node
            print(printing.data[0] + str(printing.data[1]), end=' ')

            # ノードが1つでない場合
            if self.head_node != self.tail_node:
                printing = self.head_node.next
                while(1):
                    if printing == self.tail_node:
                        print(printing.data[0] + str(printing.data[1]))
                        break
                    else:
                        print(printing.data[0] + str(printing.data[1]), end=' ')
                        printing = printing.next

    def card_to_list(self, card):
        """トランプリスト型変換メソッド

        "D7"などのトランプカードを表す文字列を第一要素がマーク(を表す文字)、第二要素がカードの数字
        であるリスト型に変換する

        Args:
            card(str): 1文字目がトランプマーク、2文字目以降がトランプの数字を表す文字列
                       (例: クラブの10 -> 'C10')

        Examples:
            >>> dll = DoublyLinkedList_for_card()
            >>> lst = dll.card_to_list('D12')
            >>> print(lst)
            ['D', 12]
        """
        lst = []
        lst.append(card[0])
        lst.append(int(card[1:]))
        return lst

    def bubble_sort_trump(self):
        """バブルソート(トランプ用)

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        双方向連結リストの全データについて、バブルソートで数字が昇順になるように並び替える

        Examples:
            >>> ins = DoublyLinkedList_for_card()
            >>> ins.insert(ins.card_to_list('C3'))
            >>> ins.insert(ins.card_to_list('D2'))
            >>> ins.insert(ins.card_to_list('S4'))
            >>> ins.insert(ins.card_to_list('C9'))
            >>> ins.insert(ins.card_to_list('H4'))
            >>> ins.bubble_sort_trump()
            >>> ins.show_trump()
            D2 C3 H4 S4 C9
        """
        flag = 1
        while (flag == 1):
            flag = 0
            # node1 -> node2の順
            node2 = self.tail_node
            node1 = node2.prev
                   
            while True:
                # nodeが1個もしくはnode2が先頭の場合
                if node1 is None:
                    break
                
                elif node2.data[1] < node1.data[1]:
                    node0 = node1.prev
                    self.swap_linked_nodes(node1, node2)
                    flag = 1
                    node1 = node0
                
                else:
                    node2 = node1
                    node1 = node1.prev

    def selection_sort_trump(self):
        """選択ソート(トランプ用)

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        双方向連結リストの全データについて、選択ソートで数字が昇順になるように並び替える

        Examples:
            >>> ins = DoublyLinkedList_for_card()
            >>> ins.insert(ins.card_to_list('C3'))
            >>> ins.insert(ins.card_to_list('D2'))
            >>> ins.insert(ins.card_to_list('S4'))
            >>> ins.insert(ins.card_to_list('C9'))
            >>> ins.insert(ins.card_to_list('H4'))
            >>> ins.selection_sort_trump()
            >>> ins.show_trump()
            D2 C3 S4 H4 C9
        """
        target = self.head_node
        while True:
            minj = target
            j = target
            while True:
                if j.data[1] < minj.data[1]:
                    minj = j
                if j == self.tail_node:
                    break
                j = j.next

            # 入れ替えが必要ない場合
            if target == minj:
                next_target = target.next
            # 隣り合うものを入れ替える場合
            elif target.next == minj:
                next_target = target
                self.swap_linked_nodes(target, minj)
            # 隣り合わないものを入れ替える場合
            else:
                next_target = target.next
                self.swap_nonlinked_nodes(target, minj)
            target = next_target
            if target == self.tail_node:
                break

    def stable_sort(self):
        """安定ソート(トランプ用)

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        双方向連結リストの全データについて、
        まずバブルソートによって整列されたカードを順番に出力し、その出力が安定であるかどうかを出力する。
        次に、選択ソートによって整列されたカードを順番に出力し、その出力が安定であるかどうかを出力する。

        Examples:
            >>> ins = DoublyLinkedList_for_card()
            >>> ins.insert(ins.card_to_list('C3'))
            >>> ins.insert(ins.card_to_list('D2'))
            >>> ins.insert(ins.card_to_list('S4'))
            >>> ins.insert(ins.card_to_list('C9'))
            >>> ins.insert(ins.card_to_list('H4'))
            >>> ins.stable_sort()
            stable sort
            D2 C3 H4 S4 C9
            Stable
            D2 C3 S4 H4 C9
            Not stable
        """
        print('stable sort')
        # オリジナルを複製
        original = DoublyLinkedList_for_card()
        p = self.tail_node
        while(1):
            original.insert(p.data)
            if p == self.head_node:
                break
            p = p.prev

        # bubble_sort
        self.bubble_sort_trump()
        self.show_trump()        
        if self.checkIsStable_DLL(original):
            print('Stable')
        else:
            print('Not stable')

        # selection_sort
        self = original
        self.selection_sort_trump()
        self.show_trump()
        if self.checkIsStable_DLL(original):
            print('Stable')
        else:
            print('Not stable')  

    def checkIsStable_DLL(self, original):
        """安定性判定メソッド

        ソート前とソート後の2つの双方向連結リストについて、安定性が保たれているかどうかを判定する。

        Args:
            original(obj): ソート前の双方向連結リスト

        Returns:
            Boolean: Trueなら安定であり、Falseなら非安定
        """
        isStable = True
        orig_n = original.head_node
        orig_m = orig_n.next
        sort_a = self.head_node
        sort_b = sort_a.next

        while True:
            while True:
                while True:
                    while True:
                        # 同じ数字があり、ソートの前後で順序が変わる場合
                        if orig_n.data[1] == orig_m.data[1] and orig_n.data == sort_b.data and orig_m.data == sort_a.data:
                            isStable = False

                        if sort_b == self.tail_node:
                            break
                        sort_b = sort_b.next
                    if sort_a == self.tail_node:
                        break
                    sort_a = sort_a.next
                if orig_m == original.tail_node:
                    break
                orig_m = orig_m.next
            if orig_n == original.tail_node:
                break
            orig_n = orig_n.next
        return isStable


class List():
    """配列クラス

    トランプ用のリストクラス(1番目の要素が文字、2番目の要素が数字(例: ['D', 3])のリストとしてデータを格納する)
    3種類のソート(バブルソート、選択ソート、挿入ソート)
    メソッドを持つ
    """

    def __init__(self, list):
        self.list = list
    
    def show(self):
        """表示用メソッド

        リストの全データをスペースを開けて表示する

        Examples:
            >>> lst = List([5,1,4])
            >>> lst.show()
            5 1 4
        """
        n = len(self.list)
        for i in range(n-1):
            print(self.list[i], end=' ')
        print(self.list[n-1])

    def insertion_sort(self, comp_func):
        """挿入ソート

        リストの要素を挿入ソートにより並び替える。
        並び替えの順序は引数comp_funcにより、
        ・昇順
        ・降順
        ・奇数>偶数かつ奇数内および偶数内では昇順
        から指定できる。
        挿入ソートの各計算ステップでの途中結果を1行ずつ表示する。

        Args:
            comp_func(ラムダ式): リストの並び替えの仕方を指定する関数
                                ・昇順(comp_func = lambda x, y: x < y)
                                ・降順comp_func = lambda x, y: x > y)
                                ・奇数>偶数かつ奇数内および偶数内では昇順
                                  (comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))

        Examples:
            >>> lst = List([5, 2, 4, 6, 1, 3])
            >>> lst.insertion_sort(comp_func = lambda x, y: x < y)
            insertion sort
            5 2 4 6 1 3
            2 5 4 6 1 3
            2 4 5 6 1 3
            2 4 5 6 1 3
            1 2 4 5 6 3
            1 2 3 4 5 6
            >>> lst.insertion_sort(comp_func = lambda x, y: x > y)
            insertion sort
            1 2 3 4 5 6
            2 1 3 4 5 6
            3 2 1 4 5 6
            4 3 2 1 5 6
            5 4 3 2 1 6
            6 5 4 3 2 1
            >>> lst.insertion_sort(comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
            insertion sort
            6 5 4 3 2 1
            5 6 4 3 2 1
            5 4 6 3 2 1
            3 5 4 6 2 1
            3 5 2 4 6 1
            1 3 5 2 4 6
        """
        print('insertion sort')
        n = len(self.list)
        self.show()
        for i in range(1, n):
            target = self.list[i]
            j = i - 1
            while (j >= 0) and (comp_func(target, self.list[j])):
                # 一つ後ろにずらす
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = target
            self.show()

    def bubble_sort(self, comp_func):
        """バブルソート

        リストの要素をバブルソートにより並び替える。
        １行目に整列された数列を出力し、2行目に交換回数を出力する。
        並び替えの順序は引数comp_funcにより、
        ・昇順
        ・降順
        ・奇数>偶数かつ奇数内および偶数内では昇順
        から指定できる。

        Args:
            comp_func(ラムダ式): リストの並び替えの仕方を指定する関数
                                ・昇順(comp_func = lambda x, y: x < y)
                                ・降順comp_func = lambda x, y: x > y)
                                ・奇数>偶数かつ奇数内および偶数内では昇順
                                  (comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
        Examples:
            >>> lst = List([5, 2, 4, 6, 1, 3])
            >>> lst.bubble_sort(comp_func = lambda x, y: x < y)
            bubble sort
            1 2 3 4 5 6
            9
            >>> lst.bubble_sort(comp_func = lambda x, y: x > y)
            bubble sort
            6 5 4 3 2 1
            15
            >>> lst.bubble_sort(comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
            bubble sort
            1 3 5 2 4 6
            12
        """
        print('bubble sort')
        n = len(self.list)
        flag = 1
        counter = 0
        while (flag == 1):
            flag = 0
            for i in range(1, n):
                j = n - i
                if comp_func(self.list[j], self.list[j - 1]):
                    tmp = self.list[j]
                    self.list[j] = self.list[j - 1]
                    self.list[j - 1] = tmp
                    flag = 1
                    counter += 1
        self.show()
        print(counter)

    def selection_sort(self, comp_func):
        """選択ソート

        リストの要素を選択ソートにより並び替える。
        １行目に整列された数列を出力し、2行目に交換回数を出力する。
        並び替えの順序は引数comp_funcにより、
        ・昇順
        ・降順
        ・奇数>偶数かつ奇数内および偶数内では昇順
        から指定できる。
        挿入ソートの各計算ステップでの途中結果を1行ずつ表示する。

        Args:
            comp_func(ラムダ式): リストの並び替えの仕方を指定する関数
                                ・昇順(comp_func = lambda x, y: x < y)
                                ・降順comp_func = lambda x, y: x > y)
                                ・奇数>偶数かつ奇数内および偶数内では昇順
                                  (comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))

        Examples:
            >>> lst = List([5, 2, 4, 6, 1, 3])
            >>> lst.selection_sort(comp_func = lambda x, y: x < y)
            selection sort
            1 2 3 4 5 6
            3
            >>> lst.selection_sort(comp_func = lambda x, y: x > y)
            selection sort
            6 5 4 3 2 1
            3
            >>> lst.selection_sort(comp_func = lambda x, y: x < y if (x+y) % 2 == 0 else (True if x % 2 == 1 else False))
            selection sort
            1 3 5 2 4 6
            4
        """
        print('selection sort')
        n = len(self.list)
        counter = 0
        for i in range(0, n):
            minj = i
            # 最小を探す
            for j in range(i, n):
                if comp_func(self.list[j], self.list[minj]):
                    minj = j
            # 入れ替え
            if minj != i:
                counter += 1
                tmp = self.list[minj]
                self.list[minj] = self.list[i]
                self.list[i] = tmp
        self.show()
        print(counter)
        

class List_for_card(List):
    """配列クラス(トランプ用)
    
    2種類のソート(バブルソート、選択ソート)及びソートの安定性を調べる
    メソッドを持つ
    """

    def bubble_sort_trump(self):
        """バブルソート(トランプ用)

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        リストの全データについて、バブルソートで数字が昇順になるように並び替える

        Examples:
            >>> ins = List_for_card([['D', 9], ['H', 2], ['C', 4]])
            >>> ins.bubble_sort_trump()
            >>> ins.show_trump()
            H2 C4 D9
        """
        n = len(self.list)
        flag = 1
        while (flag == 1):
            flag = 0
            for i in range(1, n):
                j = n - i
                if self.list[j][1] < self.list[j - 1][1]:
                    tmp = self.list[j]
                    self.list[j] = self.list[j - 1]
                    self.list[j - 1] = tmp
                    flag = 1

    def selection_sort_trump(self):
        """選択ソート(トランプ用)

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        リストの全データについて、選択ソートで数字が昇順になるように並び替える

        Examples:
            >>> ins = List_for_card([['D', 9], ['H', 2], ['C', 4]])
            >>> ins.selection_sort_trump()
            >>> ins.show_trump()
            H2 C4 D9
        """
        n = len(self.list)
        for i in range(0, n):
            minj = i
            # 最小を探す
            for j in range(i, n):
                if self.list[j][1] < self.list[minj][1]:
                    minj = j
            # 入れ替え
            tmp = self.list[minj]
            self.list[minj] = self.list[i]
            self.list[i] = tmp

    def stable_sort(self):
        """安定ソート(トランプ用)

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        リストの全データについて、
        まずバブルソートによって整列されたカードを順番に出力し、その出力が安定であるかどうかを出力する。
        次に、選択ソートによって整列されたカードを順番に出力し、その出力が安定であるかどうかを出力する。

        Examples:
            >>> ins = List_for_card([['H', 4], ['C', 9] ,['S', 4], ['D', 2], ['C', 3]])
            >>> ins.stable_sort()
            stable sort
            D2 C3 H4 S4 C9
            Stable
            D2 C3 S4 H4 C9
            Not stable
        """
        print('stable sort')
        # 元のリストを複製
        original = []
        for i in range(len(self.list)):
            original.append(self.list[i])
        
        # bubble_sort
        self.bubble_sort_trump()
        self.show_trump()
        if self.checkIsStable(original, self.list):
            print('Stable')
        else:
            print('Not stable')

        # 元のリストを複製
        self.list = original
        original = []
        for i in range(len(self.list)):
            original.append(self.list[i])

        # selection_sort
        self.selection_sort_trump()
        self.show_trump()
        if self.checkIsStable(original, self.list):
            print('Stable')
        else:
            print('Not stable')

    def checkIsStable(self, original, sorted):
        """安定性判定メソッド

        ソート前とソート後の2つのリストについて、安定性が保たれているかどうかを判定する。

        Args:
            original(list): ソート前のリスト
            sorted(list): ソート後のリスト

        Returns:
            Boolean: Trueなら安定であり、Falseなら非安定      
        """
        n = len(original)
        isStable = True
        for i in range(n):
            for j in range(i + 1, n):
                for a in range(n):
                    for b in range(a + 1, n):
                        # 同じ数字があり、ソートの前後で順序が変わる場合
                        if (original[i][1] == original[j][1] and 
                            original[i] == sorted[b] and original[j] == sorted[a]):
                            isStable = False
        return isStable
                            
    def show_trump(self):
        """トランプ表示用メソッド

        リストの1番目の要素が文字、2番目の要素が数字である(例: ['D', 3])データが格納された
        リストの全データについて、1番目と2番目の要素をつなげて(例: D3)スペースを開けて表示する。

        Examples:
            >>> ins = List_for_card([['D', 9], ['H', 2], ['C', 4]])
            >>> ins.show_trump()
            D9 H2 C4
        """
        n = len(self.list)
        for i in range(n-1):
            print(self.list[i][0] + str(self.list[i][1]), end=' ')
        print(self.list[n-1][0] + str(self.list[n-1][1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()