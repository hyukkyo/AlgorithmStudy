import heapq

def solution(operations):
    heap = []

    for operation in operations:
        command, num = operation.split()
        num = int(num)

        if command == 'I':
            heapq.heappush(heap, num)
        elif command == 'D' and heap:
            if num == 1: # 최댓값 삭제
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
            elif num == -1: # 최솟값 삭제
                heapq.heappop(heap)

    if heap:
        return [heapq.nlargest(1, heap)[0], heapq.heappop(heap)]
    else:
        return [0, 0]

    # nlargest(5, heap) = [큰 순서대로 5개 리스트를 꺼냄]
    # nlargest(5, heap, key=lambda t: t[2]) 람다식 이용도 가능