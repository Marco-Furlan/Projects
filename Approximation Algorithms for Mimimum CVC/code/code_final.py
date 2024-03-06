#Algoritmi x tesi

import random
from collections import deque

class Graph(object):
	def __init__(self, graph_dict=None, import_type=None):
		""" initializes a graph object. Examples of use: 1) Graph({1:{2,3},2:{1,3},3:{1,2}}) 2) Graph('graph_name','stb') 3)Graph('graph_name','mtx') """
		if graph_dict == None:
			graph_dict = {}
		if import_type == None:
			self.N = graph_dict
			self.E = self.all_edges() #massive time save computationally, slows down initialization
			self.V = self.all_vertices()
		if import_type == 'stb':
			self.N, self.E, self.V = self.stb_to_graph(graph_dict)
		if import_type =='mtx':
			self.N, self.E, self.V = self.mtx_to_graph(graph_dict)
		if import_type == 'mtxc':
			self.N, self.E, self.V = self.mtxc_to_graph(graph_dict)
	
	def all_vertices(self):
		return set(self.N.keys())

	def all_edges(self):
		return self.__generate_edges()
		
	def __generate_edges(self):
		edges = []
		for vertex in self.N:
			for neighbour in self.N[vertex]:
				if {neighbour, vertex} not in edges:
					edges.append({vertex, neighbour})
		return edges
		
	def stb_to_graph(self,name):
		path = '.\\_stb\\' + name + '.txt'
		str1 = open(path).read(); lst1 = str1.split('\n'); lst1.remove(''); lst2 = [l for l in lst1 if l[0]=='e']; lst3 = [l.split(' ') for l in lst2];
		for l in lst3: l.remove('e')
		for l in lst3:
			for i in range(len(l)): l[i] = int(l[i]) #convert str to int
		e=[set(l) for l in lst3]
		info = [l for l in lst1 if l[0]=='p']; info2 = [i.split(' ') for i in info]; n = int(info2[0][2])
		d = {i+1:set() for i in range(n)}
		for l in lst3:
			d[int(l[0])].add(int(l[1]))
			d[int(l[1])].add(int(l[0]))
		v = {i+1 for i in range(n)}
		return d, e, v
	
	def mtx_to_graph(self,name):
		path = '.\\_mtx\\' + name + '.txt'
		str1 = open(path).read(); lst1 = str1.split('\n'); lst1.remove(''); lst2 = lst1[2:]; lst3 = [l.split(' ') for l in lst2];
		for l in lst3:
			for i in range(len(l)): l[i] = int(l[i]) #convert str to int
		e=[set(l) for l in lst3]
		info = lst1[1]; info2 = info.split(' '); n = int(info2[0])
		d = {i+1:set() for i in range(n)}
		for l in lst3:
			d[int(l[0])].add(int(l[1]))
			d[int(l[1])].add(int(l[0]))
		v = {i+1 for i in range(n)}
		return d, e, v

	def mtxc_to_graph(self,name): #HERE!
		path = '.\\_mtx\\' + name + '.txt'
		str1 = open(path).read(); lst1 = str1.split('\n'); lst1.remove(''); lst2 = lst1[2:]; lst3 = [l.split(' ') for l in lst2];
		for l in lst3:
			for i in range(len(l)): l[i] = int(l[i]) #convert str to int
		info = lst1[1]; info2 = info.split(' '); n = int(info2[0])
		v = {i+1 for i in range(n)}
		lst4 = lst3[::-1]
		k = 0
		lst5 = []
		for i in range(n,0,-1):
			for j in range(i-1,0,-1):
				if [i,j] == lst4[k]:
					if k < len(lst4)-1:
						k += 1
				else:
					lst5.append([i,j])
		d = {i+1:set() for i in range(n)}
		e = []
		for l in lst5:
			d[int(l[0])].add(int(l[1]))
			d[int(l[1])].add(int(l[0]))
			e.append(set(l))
		return d, e, v
	
	def dfs_CVC(self):
		children = {v:set() for v in self.V}
		visited = {v:0 for v in self.V}
		def dfs_call(self,u):
			visited[u] = 1
			for v in self.N[u]:
				if visited[v] == 0:
					children[u].add(v)
					dfs_call(self,v)
		r = random.choice(list(self.V)) #root
		dfs_call(self,r)
		CVC = set()
		for v in children:
			if bool(children[v]): #exclude the leaves
				CVC.add(v)
		return CVC
	
	
	def GreedyConstruction(self):
		#inizializziamo score con i gradi dei vertici
		score = {v:len(self.N[v]) for v in self.V}
		#creiamo l'insieme RCL dei vertici di grado massimo
		max_deg = 0
		for v in self.V:
			if score[v] > max_deg:
				max_deg = score[v]
				RCL = {v}
			elif score[v] == max_deg:
				RCL.add(v)
		C = set()
		neighbourhood = set()
		edges_covered = 0
		m = len(self.E)
		while edges_covered != m:
			v = random.choice(list(RCL))
			C.add(v)
			new_neighbours = self.N[v]-C
			neighbourhood.update(new_neighbours)
			neighbourhood.discard(v)
			#aggiorniamo edges_covered
			for w in self.N[v]:
				edges_covered += not w in C
			#aggiorniamo score
			for w in new_neighbours:
				score[w] -= 1
			#aggiorniamo RCL con i vertici con score massimo
			max_score = -1
			for w in neighbourhood:
				if score[w] > max_score:
					max_score = score[w]
					RCL = {w}
				elif score[w] == max_score:
					RCL.add(w)
		return C

	def NN(self,S):
		""" returns the neighbourhood of the set S (subset of vertices). For the neighbourhood of a single vertex use edges(v) """
		N = set()
		for v in S:
			N.update(self.N[v]) #promemoria: self.edges actually returns vertices, not edges
		return N #usare update invece di N = N.union(...) ci mette 1/3 del tempo

	def is_connected_subgraph(self,C):
		""" returns whether the set C induces a connected subgraph. Faster than self.induced_subgraph(C).is_connected() """
		if not C.issubset(self.V):
			print("error in is_connected_subgraph! The vertices set is not a subset of all vertices of the graph")
			return None
		v = C.copy().pop()
		component = {v}
		vertices_to_check = {v}
		while len(vertices_to_check) > 0:
			old_component = component.copy()
			component = C&self.NN(vertices_to_check) | component #"|" is union
			vertices_to_check = component.difference(old_component)
		return len(component) == len(C)
		
	def LocalSearch(self,C):
		#inizializziamo Change
		Change = {v:1 for v in self.V}
		#inizializziamo score
		score = {v:(2*(not v in C)-1)*len(self.N[v]-C) for v in self.V}
		uncovered_edges = []
		C2 = C.copy()
		is_vertex_cover = True
		is_connected = True
		max_iterations = 100
		for i in range(max_iterations):
			if is_vertex_cover:
				if is_connected:
					if len(C) < len(C2):
						C2 = C.copy()
				else:
					return C2
				#creiamo RCL con i vertici con score massimo
				max_score = float('-inf')
				for w in C:
					if score[w] > max_score:
						max_score = score[w]
						RCL = {w}
					elif score[w] == max_score:
						RCL.add(w)
				u = random.choice(list(RCL))
				C.remove(u)
				score[u] = -score[u]
				Change[u] = 0
				#aggiorniamo Change
				for v in self.N[u]-C:
					Change[v] = 1
				#aggiorniamo score
				for v in self.N[u]:
					score[v] = score[v] - (2*(not v in C)-1) #giusta
				#aggiorniamo uncovered_edges
				for v in self.N[u]-C:
					uncovered_edges.append({u,v})
				#aggiorniamo is_vertex_cover
				is_vertex_cover = not len(uncovered_edges)
				#aggiorniamo is_connected
				is_connected = self.is_connected_subgraph(C)
				continue
			e = random.choice(uncovered_edges)
			v1,v2 = e
			if (Change[v1], Change[v2]) == (1,0): u = v1
			elif (Change[v1], Change[v2]) == (0,1): u = v2
			else:
				if score[v1] >= score[v2]: u = v1
				else: u = v2
			#u = random.choice([v1,v2])
			C.add(u)
			score[u] = -score[u]
			#aggiorniamo Change
			for v in self.N[u]-C:
				Change[v] = 1
			#aggiorniamo score
			for v in self.N[u]:
				score[v] = score[v] + (2*(not v in C)-1) #giusta
			#aggiorniamo uncovered_edges
			for v in self.N[u]-C:
				uncovered_edges.remove({u,v})
			#aggiorniamo is_vertex_cover
			is_vertex_cover = not len(uncovered_edges)
			#aggiorniamo is_connected
			is_connected = self.is_connected_subgraph(C)
		return C2
	
	def density(self):
		return 2*len(self.E)/(len(self.V) * (len(self.V)-1))
