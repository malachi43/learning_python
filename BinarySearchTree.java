public class BinarySearchTree{
    private Node root;

    public static class Node{
        private int value;
        private Node left;
        private Node right;
        private int height;

        public Node(int value){
            this.value = value;
        }
       
        public int getValue(){
            return value;
        }
    }

    public int getHeight(Node node){
        if(node == null){
            return -1;
        }
        return node.height;
    }

    public boolean isEmpty(){
        return root == null;
    }

    public void display(){
        display(root, 0);
    }

    private void display(Node node, int level) {
        if (node == null) return;
    
        display(node.right, level + 1);
    
        System.out.println("    ".repeat(level) + node.getValue());
    
        display(node.left, level + 1);
    }

    public void insert(Node node, int value){
        if(root == null){
            root = new Node(value);
            return;
        }
        if(value < node.getValue()){
            Node leftNode = node.left;
            if(leftNode == null){
               node.left = new Node(value);
            }
            else{
                insert(leftNode, value);
            }
           
        }else{
           Node rightNode = node.right;
           if(rightNode == null){
              node.right = new Node(value);
            }else{
              insert(rightNode, value);
            }
            
         }
    }

    public static void main(String[] args){
        BinarySearchTree bst = new BinarySearchTree();
        bst.insert(bst.root,15);
        bst.insert(bst.root,10);
        bst.insert(bst.root,20);
        bst.insert(bst.root,5);
        bst.insert(bst.root,12);
        bst.insert(bst.root,3);
        bst.insert(bst.root,8);
        bst.display();
    }

}


