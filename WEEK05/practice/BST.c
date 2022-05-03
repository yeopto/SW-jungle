#include <stdio.h>
#include <stdlib.h>

typedef struct _TreeNode {
    int key; // 노드 값
    struct _TreeNode *left; // 왼쪽 자식
    struct _TreeNode *right; // 오른쪽 자식
}  TreeNode;

TreeNode *search(TreeNode *root, int key) {
    if (root == NULL) {
        return NULL;
}
    if (key == root->key) { // 값을 찾음
        return root;
    }
    else if (key < root->key) {
        search(root->left, key);
    }
    else if (key > root->key) {
        search(root->right, key);
    }
}

TreeNode *insert(TreeNode *root, int key) {
    TreeNode *ptr;
    TreeNode *newNode = (TreeNode*)malloc(sizeof(TreeNode));
    newNode->key = key;
    newNode->left = newNode->right = NULL;

    if (root == NULL) { // 트리가 비어 있을 경우
        root = newNode;
        return root;
    }

    ptr = root; // root node부터 탐색 진행

    while(ptr) {
        if (key == ptr->key) {
            printf("Error : 중복값은 허용 안됨.\n");
            return root;
        } else if (key < ptr->key) {
            if (ptr->left == NULL) {
                ptr->left = newNode;
                return root;
            } else {
                ptr = ptr->left;
            }
        } else {
            if (ptr->right == NULL) {
                ptr->right = newNode;
                return root;
            } else {
                ptr = ptr->right;
            }
        }
    }
}

TreeNode *delete_node(TreeNode *root, int key) {
    TreeNode *del = NULL; // 삭제할 노드
    TreeNode *parent = NULL; // 삭제할 노드의 부모 노드
    TreeNode *successor = NULL; // 삭제할 노드의 왼쪽 서브트리에서 가장 큰 노드
    TreeNode *predecessor = NULL; // successor의 부모노드
    TreeNode *child = NULL; // 삭제할 노드의 자식 노드

    del = root;
    while (del != NULL) {
        if (key == del->key) { // 찾을 때
            break;
        }
        parent = del;
        if (key < del->key) {
            del = del->left;
        } else {
            del = del->right;
        }
    }

    if (del == NULL) {
        printf("Error : 존재하지 않는 키\n");
        return root;
    }

    if (del->left == NULL && del->right == NULL) { // 삭제할 노드의 자식노드가 없는경우
        if (parent != NULL) {
            if (parent->left == del) {
                parent->left = NULL;
            } else {
                parent->right = NULL;
            }
        } else {
            root = NULL;
        }
    } else if (del->left != NULL && del->right != NULL) { // 삭제할 노드의 자식노드가 두개인 경우
        predecessor = del;
        successor = del->left;

        while(successor->right != NULL) {
            predecessor = successor;
            successor = successor->right;
        }
        predecessor->right = successor->left;
        successor->left = del->left;
        successor->right = del->right;

        if (parent != NULL) {
            if (parent->left == del) {
                parent->left = successor;
            } else {
                parent->right = successor;
            }
        } else {
            root = successor;
        }
    } else { // 삭제할 노드의 자식 노드가 1개인 경우
        if (del->left != NULL) {
            child = del->left;
        } else {
            child = del->right;
        }

        if (parent != NULL) {
            if (parent->left == del) {
                parent->left = child;
            } else {
                parent->right = child;
            }
        } else {
            root = child;
        }
    }

    free(del);
    return root;
}

void print_tree(TreeNode* root) {
    if (root == NULL) {
        return;
    }
    printf("%d\n", root->key);
    print_tree(root->left);
    print_tree(root->right);
}

int main() {
    TreeNode *root = NULL;
    TreeNode *ptr = NULL;
    root = insert(root, 7);
    root = insert(root, 3);
    root = insert(root, 8);
    root = insert(root, 1);
    root = insert(root, 5);
    root = insert(root, 4);
    root = insert(root, 10);

    print_tree(root);
    printf("\n");

    ptr = search(root, 7);
    printf("%d\n", ptr->key);

    root = delete_node(root, 7);
    ptr = search(root, 7);

    return 0;
}