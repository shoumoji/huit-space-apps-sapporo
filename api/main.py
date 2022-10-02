from heapq import heappush, heappop


class Country:
    def __init__(self, name: str, latitude: int, longitude: int, population: int):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.population = population


class edge:
    def __init__(self, to: int, cap: int, cost: int, rev):
        self.to = to
        self.cap = cap
        self.cost = cost
        self.rev = rev


class MinCostFlow:
    INF = 10**18

    def __init__(self, V: int):
        self.V = V
        self.G = [[] for i in range(V)]
        self.dist = [self.INF]*V
        self.prevv = [0]*V
        self.preve = [None]*V

    def add_edge(self, fr: int, to: int, cap: int, cost: int) -> None:
        self.G[fr].append(edge(to, cap, cost, len(self.G[to])))
        self.G[to].append(edge(fr, 0, -cost, len(self.G[fr])-1))

    def min_cost_flow(self, s: int, t: int, f: int) -> int:
        res = 0
        h = [0]*self.V
        while f:
            pq = [(0, s)]
            dist = [self.INF]*self.V
            dist[s] = 0
            while pq:
                c, v = heappop(pq)
                if dist[v] < c:
                    continue
                for idx, e in enumerate(self.G[v]):
                    if e.cap and dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]:
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        self.prevv[e.to] = v
                        self.preve[e.to] = idx
                        heappush(pq, (dist[e.to], e.to))
            if dist[t] == self.INF:
                return -1

            for v in range(self.V):
                h[v] += dist[v]

            d = f
            v = t
            while v != s:
                d = min(d, self.G[self.prevv[v]][self.preve[v]].cap)
                v = self.prevv[v]
            f -= d
            res += d * h[t]
            v = t
            while v != s:
                self.G[self.prevv[v]][self.preve[v]].cap -= d
                self.G[v][self.G[self.prevv[v]][self.preve[v]].rev].cap += d
                v = self.prevv[v]
        return res

    def return_LOG(self, start: int):
        ret = [[0 for _ in range(self.V)] for i in range(self.V)]
        for i in range(1, self.V+1):
            for j in self.G[i]:
                if j.to > self.V+1:
                    continue
                ret[i-1][j.to-1] = start-self.G[i][j.to].cap
        return ret


class Graph:
    per = 6

    def __init__(self, n, zahyou, populations, waters):
        self.n = n
        self.G = [[float("inf") for _ in range(n)] for _ in range(n)]
        self.populations = populations
        self.waters = waters
        self.plus_minus = [0]*n
        for i in range(n):
            for j in range(n):
                self.G[i][j] = self.culc_cost(i, j, zahyou)
                self.next_path[i][j] = j
        for i in range(n):
            self.plus_minus[i] = self.culc_eval(i)

    # 2点間の輸送コストの計算
    def culc_cost(a: int, b: int, zahyou) -> int:
        return zahyou[a][b]

    # 理想からどれくらい離れているかを計算
    def culc_eval(self, idx: int) -> int:
        return self.per*self.populations[idx]-self.water[idx]


def solve(G: Graph):
    # 多点スタート&容量付き頂点の最小費用流問題に帰着

    # 水が足りていない
    mi = []
    # 水が足りている（余っている）
    pl = []
    for i in range(G.n):
        if G.plus_minus[i] >= 0:
            pl.append(i)
        else:
            mi.append(i)

    ans = MinCostFlow(2+len(mi)+2*len(pl))

    INF = 10**18

    # 始点から水が足りてない部分へ辺を張る（始点の統一）
    f = 0
    for i in mi:
        ans.add_edge(0, i+1, -G.plus_minus[i], 0)
        f -= G.plus_minus[i]

    # それぞれの点同士の間に辺を張る
    for i in range(G.n):
        for j in range(G.n):
            if i == j:
                continue
            ans.add_edge(i+1, j+1, INF, G.G[i][j])

    # 入頂点から出頂点へ辺を張る（容量付き頂点の分割）
    for idx, j in enumerate(pl):
        ans.add_edge(j+1, G.n+idx+1, G.plus_minus[j], 0)

    # 出頂点から終点へ辺を張る
    for i in range(len(pl)):
        ans.add_edge(G.n+i+1, 1+len(mi)+2*len(pl), 0)

    # フローを流す
    rec = ans.min_cost_flow(0, 1+len(mi)+2*len(pl), f)

    # LOGを返す
    LOG = ans.return_LOG(INF)
