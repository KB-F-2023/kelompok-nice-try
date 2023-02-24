#include<iostream>

using namespace std;

int N = 8;
int board[8][8];
int numQueens = 0;
int sols = 0;

void searchCol(int col) {
    // base case
    if(numQueens >= N) {
        // print solution and exit
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(board[i][j] < 1)
                	cout << "0" << "\t";
                else
					cout << board[i][j] << "\t";
            }
            cout << "\n";
        }
        cout << "\n";
        sols++;
        return;
    }

    // for each row
    for(int i = 0; i < N; i++) {
        // if cell is not attacked
        if(board[i][col] > -1) {
            // set queen and mark all cells in cross and diagonal
            board[i][col] = 1;
            for(int j = 0; j < N; j++) {
                if(j != col) board[i][j]--;
                if(j != i) board[j][col]--;
            }
            for(int j = 1; j < N; j++) {
                if(i - j >= 0 && col - j >= 0) board[i - j][col - j]--;
                if(i + j < N && col + j < N) board[i + j][col + j]--;
                if(i - j >= 0 && col + j < N) board[i - j][col + j]--;
                if(i + j < N && col - j >= 0) board[i + j][col - j]--;
            }

            numQueens++;
            searchCol(col + 1);
            // remove queens and markers
            board[i][col] = 0;
            for(int j = 0; j < N; j++) {
                if(j != col) board[i][j]++;
                if(j != i) board[j][col]++;
            }
            for(int j = 1; j < N; j++) {
                if(i - j >= 0 && col - j >= 0) board[i - j][col - j]++;
                if(i + j < N && col + j < N) board[i + j][col + j]++;
                if(i - j >= 0 && col + j < N) board[i - j][col + j]++;
                if(i + j < N && col - j >= 0) board[i + j][col - j]++;
            }
            numQueens--;
        }
    }
}

int main() {
    searchCol(0);
    cout << sols << "\n";
    return 0;
}
