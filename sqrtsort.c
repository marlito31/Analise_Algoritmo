#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

typedef struct blocks
{
    int inicio;
    int fim;
    int p;
} blocks;


void swap(int *v, int i, int j)
{
    int aux = v[i];
    v[i] = v[j];
    v[j] = aux;
}

void bubblesort(int *v, int inicio, int fim)
{
    int swapped = 1;
    for (int i = inicio; i < fim && swapped; i++)
    {
        swapped = 0;
        for (int j = inicio; j < fim - (i - inicio); j++)
        {
            if (v[j] > v[j + 1])
            {
                swap(v, j, j + 1);
                swapped = 1;
            }
        }
    }
}

void heapify(int *v, int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && v[left] > v[largest])
        largest = left;

    if (right < n && v[right] > v[largest])
        largest = right;

    if (largest != i)
    {
        swap(v, i, largest);
        heapify(v, n, largest);
    }
}

void heapSort(int *v, int start, int end)
{
    int n = end - start + 1;

    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(v + start, n, i);

    for (int i = n - 1; i > 0; i--)
    {
        swap(v, start, start + i);
        heapify(v + start, i, 0);
    }
}

void merge(int *v, blocks *b, int n, int qtd_blocks)
{

    int *f = malloc(sizeof(int) * n);

    int maior;

    for (int i = 0, index_f = n - 1; i < n; i++, index_f--)
    {
        maior = 0;
        int index_p = 0;
        for (int j = 0; j < qtd_blocks; j++)
        {
            if (b[j].p > maior && b[j].fim >= b[j].inicio)
            {
                maior = b[j].p;
                index_p = j;
            }
        }
        f[index_f] = maior;
        b[index_p].fim--;
        b[index_p].p = v[b[index_p].fim];
    }


}

void sqrtsort_bubble(int *v, int n)
{
    int size = (int)sqrt(n);

    int qtd_blocks = (n / size) + 1;

    blocks *b = malloc(sizeof(blocks) * qtd_blocks);

    for (int i = 0, j = 0; i < n; i += size, j++)
    {
        int fim;
        if (i + size - 1 < n)
        {
            fim = i + size - 1;
        }
        else
        {
            fim = n - 1;
        }

        bubblesort(v, i, fim);

        b[j].fim = fim;
        b[j].inicio = i;
        b[j].p = v[fim];
    }

    merge(v, b, n, qtd_blocks);
}

void sqrtsort_heapsort(int *v, int n)
{
    int size = (int)sqrt(n);

    int qtd_blocks = (n / size) + 1;

    blocks *b = malloc(sizeof(blocks) * qtd_blocks);

    for (int i = 0, j = 0; i < n; i += size, j++)
    {
        int fim;
        if (i + size - 1 < n)
        {
            fim = i + size - 1;
        }
        else
        {
            fim = n - 1;
        }

        heapSort(v, i, fim);

        b[j].fim = fim;
        b[j].inicio = i;
        b[j].p = v[fim];
    }

    merge(v, b, n, qtd_blocks);
}

int main()
{

    int k[5] = {10000, 100000, 1000000, 10000000, 100000000};

    FILE *file = fopen("resultado_experimento.txt", "w");

    for (int j = 0; j < 5; j++)
    {
        int aux = 0;
        int n = k[j];

        int *b = malloc(sizeof(int) * n);
        int *h = malloc(sizeof(int) * n);

        srand(time(0));
        for (int i = 0; i < n; i++)
        {
            aux = rand() % 100000000;
            b[i] = aux;
            h[i] = aux;
        }

        clock_t t;

        fprintf(file, "\n Bubble Sort (n = 10^%d):\n", j + 4);
        t = clock();
        sqrtsort_bubble(b, n);
        t = clock() - t;
        fprintf(file, "%.5f seconds\n", ((float)t) / CLOCKS_PER_SEC);

        fprintf(file, "\n Heap Sort (n = 10^%d):\n", j + 4);
        t = clock();
        sqrtsort_heapsort(h, n);
        t = clock() - t;
        fprintf(file, "%.5f seconds\n", ((float)t) / CLOCKS_PER_SEC);
    }

    return 0;
}
