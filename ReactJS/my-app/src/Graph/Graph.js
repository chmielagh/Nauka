import GraphView from 'react-digraph'
import React, {Component} from 'react'
import Radium from 'radium'


const EmptyShape = (
    <symbol viewBox="0 0 100 100" id="empty">
      <circle cx="50" cy="50" r="45"></circle>
    </symbol>
  )
  
  const SpecialShape = (
    <symbol viewBox="0 0 100 100" id="special">
      <rect transform="translate(50) rotate(45)" width="70" height="70"></rect>
    </symbol>
  )
  
  const SpecialChildShape = (
    <symbol viewBox="0 0 100 100" id="specialChild">
      <rect x="2.5" y="0" width="95" height="97.5" fill="rgba(30, 144, 255, 0.12)"></rect>
    </symbol>
  )
  
  const EmptyEdgeShape = (
    <symbol viewBox="0 0 50 50" id="emptyEdge">
      <circle cx="25" cy="25" r="8" fill="currentColor"> </circle>
    </symbol>
  )
  
  const SpecialEdgeShape = (
    <symbol viewBox="0 0 50 50" id="specialEdge">
      <rect transform="rotate(45)"  x="25" y="-4.5" width="15" height="15" fill="currentColor"></rect>
    </symbol>
  )


const GraphConfig =  {
    NodeTypes: {
        empty: {
          typeText: "None",
          shapeId: "#empty",
          shape: EmptyShape
        },
        special: {
          typeText: "Special",
          shapeId: "#special",
          shape: SpecialShape
        }
      }, 
      NodeSubtypes: {
        specialChild: {
          shapeId: "#specialChild",
          shape: SpecialChildShape
        }
      }, 
      EdgeTypes: {
        emptyEdge: {
          shapeId: "#emptyEdge",
          shape: EmptyEdgeShape
        },
        specialEdge: {
          shapeId: "#specialEdge",
          shape: SpecialEdgeShape
        }
      }
}

const NODE_KEY = "id" // Key used to identify nodes

// These keys are arbitrary (but must match the config)
// However, GraphView renders text differently for empty types
// so this has to be passed in if that behavior is desired.
const EMPTY_TYPE = "empty"; // Empty node type
const SPECIAL_TYPE = "special"; 
const SPECIAL_CHILD_SUBTYPE = "specialChild";
const EMPTY_EDGE_TYPE = "emptyEdge";
const SPECIAL_EDGE_TYPE = "specialEdge";

const styles = {
    graph: {
      height: '100%',
      width: '100%',
    }
  };

  const sample = {
    "nodes": [
      {
        "id": 1,
        "title": "Node A",
        "x": 258.3976135253906,
        "y": 331.9783248901367,
        "type": SPECIAL_TYPE
      },
      {
        "id": 2,
        "title": "Node B",
        "x": 593.9393920898438,
        "y": 260.6060791015625,
        "type": EMPTY_TYPE,
        "subtype": SPECIAL_CHILD_SUBTYPE
      },
      {
        "id": 3,
        "title": "Node C",
        "x": 237.5757598876953,
        "y": 61.81818389892578,
        "type": EMPTY_TYPE
      },
      {
        "id": 4,
        "title": "Node C",
        "x": 600.5757598876953,
        "y": 600.81818389892578,
        "type": EMPTY_TYPE
      }
    ],
    "edges": [
      {
        "source": 1,
        "target": 2,
        "type": SPECIAL_EDGE_TYPE
      },
      {
        "source": 2,
        "target": 4,
        "type": EMPTY_EDGE_TYPE
      }
    ]
  }

class Graph extends Component {

  constructor(props) {
    super(props);

    this.state = {
      graph: sample,
      selected: {}
    }
  }

  getNodeIndex(searchNode) {
    return this.state.graph.nodes.findIndex((node)=>{
      return node[NODE_KEY] === searchNode[NODE_KEY]
    })
  }

  // Helper to find the index of a given edge
  getEdgeIndex(searchEdge) {
    return this.state.graph.edges.findIndex((edge)=>{
      return edge.source === searchEdge.source &&
        edge.target === searchEdge.target
    })
  }

  // Given a nodeKey, return the corresponding node
  getViewNode = nodeKey => {
    const searchNode = {};
    searchNode[NODE_KEY] = nodeKey;
    const i = this.getNodeIndex(searchNode);
    return this.state.graph.nodes[i]
  }

  /*
   * Handlers/Interaction
   */

  // Called by 'drag' handler, etc.. 
  // to sync updates from D3 with the graph
  onUpdateNode = viewNode => {
    const graph = this.state.graph;
    const i = this.getNodeIndex(viewNode);

    graph.nodes[i] = viewNode;
    this.setState({graph: graph});
  }

  // Node 'mouseUp' handler
  onSelectNode = viewNode => {
    // Deselect events will send Null viewNode
    if (!!viewNode){
      this.setState({selected: viewNode});
    } else{
      this.setState({selected: {}});
    }
  }

  // Edge 'mouseUp' handler
  onSelectEdge = viewEdge => {
    this.setState({selected: viewEdge});
  }

  // Updates the graph with a new node
  onCreateNode = (x,y) => {
    const graph = this.state.graph;

    // This is just an example - any sort of logic 
    // could be used here to determine node type
    // There is also support for subtypes. (see 'sample' above)
    // The subtype geometry will underlay the 'type' geometry for a node
    const type = EMPTY_TYPE;

    const viewNode = {
      id: this.state.graph.nodes.length + 1,
      title: '',
      type: type,
      x: x,
      y: y
    }

    graph.nodes.push(viewNode);
    this.setState({graph: graph});
  }

  // Deletes a node from the graph
  onDeleteNode = viewNode => {
    const graph = this.state.graph;
    const i = this.getNodeIndex(viewNode);
    graph.nodes.splice(i, 1);

    // Delete any connected edges
    const newEdges = graph.edges.filter((edge, i)=>{
      return  edge.source !== viewNode[NODE_KEY] && 
              edge.target !== viewNode[NODE_KEY]
    })

    graph.edges = newEdges;

    this.setState({graph: graph, selected: {}});
  }

  // Creates a new node between two edges
  onCreateEdge = (sourceViewNode, targetViewNode) => {
    const graph = this.state.graph;

    // This is just an example - any sort of logic 
    // could be used here to determine edge type
    const type = EMPTY_EDGE_TYPE;

    const viewEdge = {
      source: sourceViewNode[NODE_KEY],
      target: targetViewNode[NODE_KEY],
      type: type
    }
    
    // Only add the edge when the source node is not the same as the target
    if (viewEdge.source !== viewEdge.target) {
      graph.edges.push(viewEdge);
      this.setState({graph: graph});
    }
  }

  // Called when an edge is reattached to a different target.
  onSwapEdge = (sourceViewNode, targetViewNode, viewEdge) => {
    const graph = this.state.graph;
    const i = this.getEdgeIndex(viewEdge);
    const edge = JSON.parse(JSON.stringify(graph.edges[i]));

    edge.source = sourceViewNode[NODE_KEY];
    edge.target = targetViewNode[NODE_KEY];
    graph.edges[i] = edge;

    this.setState({graph: graph});
  }

  // Called when an edge is deleted
  onDeleteEdge = viewEdge => {
    const graph = this.state.graph;
    const i = this.getEdgeIndex(viewEdge);
    graph.edges.splice(i, 1);
    this.setState({graph: graph, selected: {}});
  }

  /* Define custom graph editing methods here */

  render() {
    const nodes = this.state.graph.nodes;
    const edges = this.state.graph.edges;
    const selected = this.state.selected;

    const NodeTypes = GraphConfig.NodeTypes;
    const NodeSubtypes = GraphConfig.NodeSubtypes;
    const EdgeTypes = GraphConfig.EdgeTypes;

    return (
      <div id='graph' style={styles.graph}>

        <GraphView  ref='GraphView'
                    nodeKey={NODE_KEY}
                    emptyType={EMPTY_TYPE}
                    nodes={nodes}
                    edges={edges}
                    selected={selected}
                    nodeTypes={NodeTypes}
                    nodeSubtypes={NodeSubtypes}
                    edgeTypes={EdgeTypes}
                    getViewNode={this.getViewNode}
                    onSelectNode={this.onSelectNode}
                    onCreateNode={this.onCreateNode}
                    onUpdateNode={this.onUpdateNode}
                    onDeleteNode={this.onDeleteNode}
                    onSelectEdge={this.onSelectEdge}
                    onCreateEdge={this.onCreateEdge}
                    onSwapEdge={this.onSwapEdge}
                    onDeleteEdge={this.onDeleteEdge}/>
      </div>
    );
  }

}
export default Radium(Graph);