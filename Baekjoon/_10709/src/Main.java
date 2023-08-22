import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer hwInput = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(hwInput.nextToken());
        int w = Integer.parseInt(hwInput.nextToken());

        String[] sky = new String[h];
        int[][] answer = new int[h][w];

        for (int i = 0; i < h; i++) {
            sky[i] = br.readLine();

            boolean isFirstCloud = true;
            int count = 1;
            for (int j = 0; j < w; j++) {
                if (isFirstCloud) {
                    if (sky[i].charAt(j) == '.') {
                        answer[i][j] = -1;
                    } else {
                        answer[i][j] = 0;
                        isFirstCloud = false;
                    }
                } else {
                    if (sky[i].charAt(j) == '.') {
                        answer[i][j] = count++;
                    } else {
                        answer[i][j] = 0;
                        count = 1;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                sb.append(answer[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}