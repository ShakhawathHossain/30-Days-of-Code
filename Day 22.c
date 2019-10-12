#include <stdio.h>
#include <stdlib.h>
typedef struct Node{
    struct Node* left;
    struct Node* right;
    int data;
}Node;
Node* newNode(int data){
    Node* node=(Node*)malloc(sizeof(Node));
    node->left=node->right=NULL;
    node->data=data;
    return node;
}

int getHeight(Node* root){
    int l=0,r=0;
    if (root==NULL)
    {
        return -1;
    }

    /*else
    {
        Node* temp=root;
        while(temp->left!=NULL)
        {
            temp=temp->left;
            l++;
        }
        Node* temp1=root;
        while(temp1->right!=NULL)
        {
            temp1=temp1->right;
            r++;
        }
    }*/
     l = 1 + getHeight(root->left);
     r = 1 + getHeight(root->right);
    return (r>l)? r:l;
}

Node* insert(Node* root,int data){
    if(root==NULL)
        return newNode(data);
    else{
        Node* cur;
        if(data<=root->data){
            cur=insert(root->left,data);
            root->left=cur;
        }
        else{
            cur=insert(root->right,data);
            root->right=cur;
        }

    }
    return root;
}
int main(){
    Node* root=NULL;
    int T,data;
    scanf("%d",&T);
    while(T-->0){
        scanf("%d",&data);
        root=insert(root,data);
    }
    int height=getHeight(root);
    printf("%d",height);
    return 0;

}
