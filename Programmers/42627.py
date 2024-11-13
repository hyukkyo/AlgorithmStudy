import heapq

def solution(jobs):
    min_heap = []

    answer = 0
    current_time = 0
    start = -1

    # 핵심
    # 현재 시각에서 시작가능한 프로세스들 중에서, 소요시간이 가장 짧은 프로세스를 실행하면 됨