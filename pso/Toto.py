solution = [ ("B", "A"), ("B", "C"), ("C", "B"), ("A", "B")]
#solution = [("A", "B"), ("D", "C"), ("B", "A"), ("A", "D"), ("D", "A")]
#solution = [("D", "C"), ("B", "C"), ("C", "A"), ("C", "D"), ("A", "B")]
#solution = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "A"), ("C", "A"), ("D", "A")]

def countEdges(graph):
	result = {}
	for (start, dest) in graph:
		if start in result:
			result[start] = result[start] + 1
		else:
			result[start] = 1
	return result

def orderSolution(graph, startNode, isFirst = True):
	result = []
	countMap = countEdges(graph)
	curPostion = startNode
	flag = True
	subGraph = []
	while flag is True:
		flag = False
		for (start, dest) in graph:
			if curPostion is start:
				i = countMap[start]
				graph.remove((start, dest))
				while i > 1:
					subGraph.append(orderSolution(graph, start, False))
					i = i - 1
				for item in subGraph:
					if len(item) != 0 and item[len(item) - 1][1] is not startNode:
						result += item
						subGraph.remove(item)
				result.append((start, dest))
				curPostion = dest
				flag = True
	for item in subGraph:
		result += item
	if isFirst and (len(graph) != 0 or result[len(result) - 1][1] != startNode):
		raise Exception("Invalid Graph")
	return result

print solution
result = orderSolution(solution, "A")
print result

#class Abs:
#	def run(self):
#		self.update()
#		
#	def update(self):
#		print "ABS -> update"
#
#class FirstImplem(Abs):
#
#	def run(self):
#		self.update()
#	
##	def update(self):
##		print "FirstImplem -> update"
#
#a = FirstImplem()
#a.update()
