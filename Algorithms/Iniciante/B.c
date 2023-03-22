#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x, y, id;
} token;

typedef struct {
    int a, b, id;
} player;

int cmp_token(const void *a, const void *b) {
    token *t1 = (token *) a;
    token *t2 = (token *) b;
    if (t1->x != t2->x) {
        return t1->x - t2->x;
    } else {
        return t1->y - t2->y;
    }
}

int cmp_player(const void *a, const void *b) {
    player *p1 = (player *) a;
    player *p2 = (player *) b;
    if (p1->a != p2->a) {
        return p1->a - p2->a;
    } else {
        return p1->b - p2->b;
    }
}

int cmp_token_id(const void *a, const void *b) {
    token *t1 = (token *) a;
    token *t2 = (token *) b;
    return t1->id - t2->id;
}

int main() {
    // read input
    int t;
    scanf("%d", &t);
    token tokens[t];
    for (int i = 0; i < t; i++) {
        scanf("%d %d", &tokens[i].x, &tokens[i].y);
        tokens[i].id = i + 1;
    }
    int p;
    scanf("%d", &p);
    player players[p];
    for (int i = 0; i < p; i++) {
        scanf("%d %d", &players[i].a, &players[i].b);
        players[i].id = i + 1;
    }

    // sort tokens and players
    qsort(tokens, t, sizeof(token), cmp_token);
    qsort(players, p, sizeof(player), cmp_player);

    // process each player
    int player_index = 0;
    int tokens_received[p][t]; // 2D array to store the received tokens for each player
    int num_received[p]; // array to store the number of received tokens for each player
    for (int i = 0; i < p; i++) {
        num_received[i] = 0;
    }
    while (player_index < p) {
        int next_player_index = player_index + 1;
        while (next_player_index < p && players[next_player_index].a == players[player_index].a && players[next_player_index].b == players[player_index].b) {
            next_player_index++;
        }
        int tokens_received_for_player[t];
        int num_received_for_player = 0;
        int token_index = 0;
        while (token_index < t && tokens[token_index].x * players[player_index].a + players[player_index].b > tokens[token_index].y) {
            token_index++;
        }
        while (token_index < t && (next_player_index == p || tokens[token_index].x * players[player_index].a + players[player_index].b <= tokens[token_index].y * players[next_player_index].a + players[next_player_index].b)) {
            tokens_received_for_player[num_received_for_player] = tokens[token_index].id;
            num_received_for_player++;
            token_index++;
        }
        for (int i = player_index; i < next_player_index; i++) {
            num_received[i] = num_received_for_player;
            for (int j = 0; j < num_received_for_player; j++) {
                int token_id = received_tokens_for_player[j];
                player_tokens[i].push_back(token_id);
            }
            player_index = next_player_index;
        }
        for (int i = 0; i < num_players; i++) {
            printf("%d", (int)player_tokens[i].size());
            for (int j = 0; j < player_tokens[i].size(); j++) {
                printf(" %d", player_tokens[i][j]);
            }
            printf("\n");
        }
    }
}
