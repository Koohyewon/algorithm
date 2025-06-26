import sys

sys.setrecursionlimit(10**6)  # 이 줄을 제거해도 동작

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))

stack = []
output = []

# 스택을 활용한 트리 구성 및 후위 순회 시뮬레이션
def solve():
    stack = []
    for value in preorder:
        node = {'val': value, 'left': None, 'right': None}
        if not stack:
            stack.append(node)
            continue

        # 새 노드가 스택 top보다 작으면 왼쪽 자식
        if value < stack[-1]['val']:
            stack[-1]['left'] = node
        else:
            # 새 노드가 스택 top보다 크면, 적절한 부모 찾기
            parent = None
            while stack and stack[-1]['val'] < value:
                parent = stack.pop()
            parent['right'] = node
        stack.append(node)

    def postorder(node):
        if node is None:
            return
        postorder(node['left'])
        postorder(node['right'])
        print(node['val'])

    root = {'val': preorder[0], 'left': None, 'right': None}
    stack = [root]
    for value in preorder[1:]:
        node = {'val': value, 'left': None, 'right': None}
        if value < stack[-1]['val']:
            stack[-1]['left'] = node
            stack.append(node)
        else:
            parent = None
            while stack and stack[-1]['val'] < value:
                parent = stack.pop()
            parent['right'] = node
            stack.append(node)

    postorder(root)

solve()
