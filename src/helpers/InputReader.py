import collections

from src.DIMACSGraph import DIMACSGraph


class InputReader:

    edge = collections.namedtuple('edge', ['e', 'vertex', 'adjacent'])
    header = collections.namedtuple('edge', ['p', 'format', 'nodes', 'edges'])

    @staticmethod
    def read(file):
        """
        Read the DIMACS .col file and creates an new
        DIMACSGraph instance that represents the graph
        inside the file.

        :param file: An DIMACS graph instance .col file
        :return: new DIMACSGraph instance
        """
        with open(file) as content:
            content_read = content.read()
            content_list = content_read[content_read.index('p edge'):].split('\n')
            headers = InputReader.header._make(content_list[0].split(' '))
            split_list = [item.split(' ') for item in content_list[1:]]
            edges_list = [InputReader.edge._make(item) for item in split_list if len(item) == 3]
            return DIMACSGraph(headers.nodes, headers.edges, edges_list)
