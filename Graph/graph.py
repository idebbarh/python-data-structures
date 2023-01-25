class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.graph_dis = {}
        for start, end, d in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
                self.graph_dis[start+" To "+end] = d
            else:
                self.graph_dict[start] = [end]
                self.graph_dis[start+" To "+end] = d
        print("Graph Dict:", self.graph_dict)
        print("Graph Distance:", self.graph_dis)

    def calc_distance(self,start,end,path=[],dis=0) :
        path = path + [start]
        if len(path) > 1 :
            disPath = path[-2]+" To "+path[-1]
            if disPath in self.graph_dis :
                dis +=self.graph_dis[disPath]

        if start == end :
            path.append(dis)
            return [path]

        if start not in self.graph_dict :
            return [],0

        paths = []

        for node in self.graph_dict[start] :
            if node not in path :
                new_path = self.calc_distance(node,end,path,dis)
                for p in new_path :
                    paths.append(p)

        return paths


    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    if p not in paths :
                        paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == '__main__':


    routes = [
        ("Mumbai", "Paris",1500),
        ("Mumbai", "Dubai",1300),
        ("Paris", "Dubai",3000),
        ("Paris", "Mumbai",8500),
        ("Paris", "New York",4000),
        ("Dubai", "New York",1400),
        ("New York", "Toronto",7800),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"
    strPaths = ''
    print(f"All Paths Between {start} And {end} :")
    for i,p in enumerate(route_graph.get_paths(start,end)) :
        strPaths+=str(i+1)+"-"+"==>".join(p)+"\n"
    print(strPaths)

    print(f"All Paths Between {start} And {end} With Distance :")
    strPathsWithDis = ""
    for i,p in enumerate(route_graph.calc_distance(start,end)) :
        strPathsWithDis+=str(i+1)+"-"
        for c in range(len(p)) :
            strPathsWithDis+=p[c]+"==>" if c != len(p)-1 and c!= len(p)-2 else ("\n-Totale Distance Is : "+str(p[c])+"Km"+"\n" if c == len(p)-1 else p[c])

    print(strPathsWithDis)