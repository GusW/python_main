#!/usr/bin/env python3
""" Solution: Multiply two matrices """

import random
import time
import math
import multiprocessing as mp


def seq_matrix_multiply(A, B):
    """sequential implementation of matrix multiplication"""
    # establish a few useful variables
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])
    if num_cols_A != num_rows_B:
        raise ArithmeticError(
            "Invalid dimensions; Cannot multiply {}x{}*{}x{}".format(
                num_rows_A, num_cols_A, num_rows_B, num_cols_B
            )
        )
    # compute a return matrix product C = A*B
    C = [[0] * num_cols_B for i in range(num_rows_A)]
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            for k in range(num_cols_A):  # same as num_rows_B
                C[i][j] += A[i][k] * B[k][j]
    return C


def par_matrix_multiply(A, B):
    """parallel implementation of matrix multiplication"""
    # establish a few useful variables
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])
    if num_cols_A != num_rows_B:
        raise ArithmeticError(
            "Invalid dimensions; Cannot multiply {}x{}*{}x{}".format(
                num_rows_A, num_cols_A, num_rows_B, num_cols_B
            )
        )

    # if the output C will be small enough, simply use the sequential version
    if num_rows_A * num_cols_B < 25_000:
        return seq_matrix_multiply(A, B)

    # create workers to calculate results for subset of rows in C
    num_workers = mp.cpu_count()
    chunk_size = math.ceil(num_rows_A / num_workers)
    C_1D = mp.RawArray("d", num_rows_A * num_cols_B)  # flat version of matrix C

    workers = []
    for w in range(num_workers):
        row_start_C = min(w * chunk_size, num_rows_A)
        row_end_C = min((w + 1) * chunk_size, num_rows_A)
        workers.append(
            mp.Process(target=_par_worker, args=(A, B, C_1D, row_start_C, row_end_C))
        )

    for w in workers:
        w.start()
    for w in workers:
        w.join()

    # convert flat C_1D into 2D list-of-lists
    C_2D = [[0] * num_cols_B for i in range(num_rows_A)]
    for i in range(num_rows_A):
        for j in range(num_cols_B):
            C_2D[i][j] = C_1D[i * num_cols_B + j]
    return C_2D


def _par_worker(A, B, C_1D, row_start_C, row_end_C):
    """parallel worker to calculate results for subset of rows in C"""
    cols_size_b = len(B[0])
    cols_size_a = len(A[0])
    for i in range(row_start_C, row_end_C):  # subset of rows in A
        for j in range(cols_size_b):  # num_cols_B
            for k in range(cols_size_a):  # num_cols_A, also num_rows_B
                C_1D[i * cols_size_b + j] += A[i][k] * B[k][j]


if __name__ == "__main__":
    NUM_EVAL_RUNS = 1
    ROW_SIZE = 500
    COL_SIZE = 400

    A = [[random.random() for i in range(COL_SIZE)] for j in range(ROW_SIZE)]
    B = [[random.random() for i in range(ROW_SIZE // 2)] for j in range(COL_SIZE)]

    print("Evaluating Sequential Implementation...")
    sequential_result = seq_matrix_multiply(A, B)  # "warm up"
    sequential_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        seq_matrix_multiply(A, B)
        sequential_time += time.perf_counter() - start
    sequential_time /= NUM_EVAL_RUNS

    print("Evaluating Parallel Implementation...")
    parallel_result = par_matrix_multiply(A, B)  # "warm up"
    parallel_time = 0
    for i in range(NUM_EVAL_RUNS):
        start = time.perf_counter()
        par_matrix_multiply(A, B)
        parallel_time += time.perf_counter() - start
    parallel_time /= NUM_EVAL_RUNS

    if sequential_result != parallel_result:
        raise Exception("sequential_result and parallel_result do not match.")
    print("Average Sequential Time: {:.2f} ms".format(sequential_time * 1000))
    print("Average Parallel Time: {:.2f} ms".format(parallel_time * 1000))
    print("Speedup: {:.2f}".format(sequential_time / parallel_time))
    print(
        "Efficiency: {:.2f}%".format(
            100 * (sequential_time / parallel_time) / mp.cpu_count()
        )
    )
