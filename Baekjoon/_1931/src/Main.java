import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] time = new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            time[i][0] = Integer.parseInt(st.nextToken()); // 0은 시작시간
            time[i][1] = Integer.parseInt(st.nextToken()); // 1은 종료시간
        }

        // 그리디 알고리즘
        // 종료 시간을 기준으로 정렬하고, 가장 먼저 끝나는 회의부터 픽한다.

        // 2차원 배열은 Arrays.sort()로 그냥 정렬이 안됨
        // Comparator 익명클래스 구현, 또는 람다식을 통해 정렬해야 함
        // Comparator을 이용한 방법

        Arrays.sort(time, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] == o2[1]) { // 종료시간이 같으면
                    return o1[0] - o2[0]; // 시작시간 기준 오름차순
                }
                return o1[1] - o2[1]; // 종료시간 기준 오름차순
            }
        });

        int count = 0;
        int previousEndTime = 0;

        for (int i = 0; i < N; i++) {
            if (previousEndTime <= time[i][0]) {
                previousEndTime = time[i][1];
                count++;
            }
        }

        System.out.println(count);
    }
}