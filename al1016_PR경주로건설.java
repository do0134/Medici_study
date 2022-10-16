import java.util.LinkedList;
import java.util.Queue;

public class al1016_PR경주로건설 {

	// 방향배열
	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { -1, 0, 1, 0 };

	static int N;
	static int[][][] visited;
	static int min = Integer.MAX_VALUE;

	// 일단 클래스를 만들게
	// x좌표, y좌표, 어디로 들어왔는지, 지금까지 누적금액 얼만지
	class Load {
		int x;
		int y;
		int d; // 방향
		int cost;

		Load(int x, int y, int d, int cost) {
			this.x = x;
			this.y = y;
			this.d = d;
			this.cost = cost;
		}

	}

	public int solution(int[][] board) {
		N = board.length;
		visited = new int[N][N][4];

		int answer = bfs(board);
		return answer;
	}

	// bfs 시나리오 돌리기
	// 도착지점에서의 최솟값을 반환한다
	public int bfs(int[][] board) {
		// 갈만한 장소를 등록해두는 que
		Queue<Load> que = new LinkedList<>();
		que.add(new Load(0, 0, -1, 0));
		visited[0][0][0] = 1;
		visited[0][0][1] = 1;
		visited[0][0][2] = 1;
		visited[0][0][3] = 1;

		while (!que.isEmpty()) {
			Load current = que.poll();
			int cx = current.x; // 출발지점
			int cy = current.y; // 출발지점
			int cd = current.d; // 들어온 방향
			int ccost = current.cost;

			// 만약 도착점에 도달했다면 비용 체크
			if (cx == N - 1 && cy == N - 1) {
				min = Math.min(min, ccost);
				continue; // 갱신도 마쳤으니까 다음 사이클로 이동
			}

			for (int i = 0; i < 4; i++) {
				int dr = cx + dx[i]; // 목표지점
				int dc = cy + dy[i]; // 목표지점
				int dd = i; // 나갈 방향
				int dcost;

				if (dr < 0 || dc < 0 || dr >= N || dc >= N || board[dr][dc] == 1) {
					continue; // 못쓰는 길이니까 다음 for문 사이클로 이동
				}

				if (cd == -1 || cd == dd) {
					// 출발 시점이거나 들어온 방향과 나가는 방향이 같음 (직진)
					dcost = ccost + 100;
				} else {
					// 들어온 방향과 나가는 방향이 다름 (코너)
					dcost = ccost + 600;
				}

				if (cd==-1) {
					visited[dr][dc][0]=dcost;
					visited[dr][dc][1]=dcost;
					visited[dr][dc][2]=dcost;
					visited[dr][dc][3]=dcost;
					que.add(new Load(dr, dc, dd, dcost));
				} else if (visited[dr][dc][cd] == 0) {
					// 첫방문일 경우
					visited[dr][dc][cd] = dcost;
					que.add(new Load(dr, dc, dd, dcost));
				} else if (visited[dr][dc][cd] >= dcost) {
					// 방문 기록은 있는데 방금 탄 루트보다 비싸거나 같은 경우
					// 같은 경우에도 앞으로 어떻게 될지 모르니까 넣어준다
					visited[dr][dc][cd] = dcost;
					que.add(new Load(dr, dc, dd, dcost));
				}

			}

		}

		return min;
	}

}
