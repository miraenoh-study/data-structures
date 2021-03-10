# SparseMatrix의 메소드 mmult에서 SparseMatrix를 어노테이션 하기 위해 임포트
# It will become the default in Python 3.10.
from __future__ import annotations


class Term:
    def __init__(self, row: int, col: int, value: int):
        self.row = row
        self.col = col
        self.value = value


class SparseMatrix:
    def __init__(self, n_rows: int, n_cols: int, n_terms: int, terms: list[Term]):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_terms = n_terms
        self.terms = terms

    def print(self):
        terms = self.terms[:]
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if len(terms) and terms[0].row == row and terms[0].col == col:
                    print(terms[0].value, end='\t')
                    terms.pop(0)
                else:
                    print('0', end='\t')
            print()

    def transpose(self) -> SparseMatrix:
        # A new matrix to save the transposed matrix
        transposed_matrix = SparseMatrix(
            self.n_cols, self.n_rows, self.n_terms, [])

        if self.n_terms == 0:
            return transposed_matrix

        # Transpose all terms of the original matrix from the col 0
        for i in range(0, self.n_cols):
            for term in self.terms:
                if term.col == i:
                    transposed_matrix.terms.append(
                        Term(term.col, term.row, term.value))

        return transposed_matrix

    def fast_transpose(self) -> SparseMatrix:
        # A new matrix to save the transposed matrix
        transposed_matrix = SparseMatrix(
            self.n_cols, self.n_rows, self.n_terms, [None for _ in range(self.n_terms)])

        if self.n_terms == 0:
            return transposed_matrix

        # The number of each col's terms
        row_terms = [0 for i in range(self.n_cols)]
        for term in self.terms:
            row_terms[term.col] += 1

        # The starting positions of each col
        starting_pos = [0]
        for i in range(1, self.n_cols):
            starting_pos.append(starting_pos[i - 1] + row_terms[i - 1])

        # Transpose all terms of the original matrix from the col 0
        for i in range(self.n_terms):
            term = self.terms[i]

            # Get the index for the terms list of transposed matrix and adjust the starting_pos list
            j = starting_pos[term.col]
            starting_pos[term.col] += 1

            transposed_matrix.terms[j] = Term(
                term.col, term.row, term.value)

        # Done. Return the transposed matrix
        return transposed_matrix

    @staticmethod
    def madd(matrix_a: SparseMatrix, matrix_b: SparseMatrix) -> SparseMatrix:
        # Check if the dimensions are identical
        if (matrix_a.n_rows != matrix_b.n_rows) or (matrix_a.n_cols != matrix_b.n_cols):
            print('Incompatible matrices')
            raise SystemExit

        # Initialize the result matrix
        result = SparseMatrix(matrix_a.n_rows, matrix_a.n_rows, 0, [])

        a_terms = matrix_a.terms[:]
        b_terms = matrix_b.terms[:]
        while len(a_terms) or len(b_terms):
            # The first terms of matrixes
            a_term = a_terms[0] if len(a_terms) else None
            b_term = b_terms[0] if len(b_terms) else None

            if not a_term:
                result.terms.append(b_term)
                b_terms.pop(0)
            elif not b_term:
                result.terms.append(a_term)
                a_terms.pop(0)
            else:
                # Both terms exist
                # Compare which term comes first
                if a_term.row == b_term.row and a_term.col == b_term.col:
                    # Both term located in the same position
                    # Add the values
                    result.terms.append(
                        Term(a_term.row, a_term.col, a_term.value + b_term.value))
                    a_terms.pop(0)
                    b_terms.pop(0)
                elif a_term.row <= b_term.row and a_term.col < b_term.col:
                    # A term comes first
                    result.terms.append(a_term)
                    a_terms.pop(0)
                else:
                    # B term comes first
                    result.terms.append(b_term)
                    b_terms.pop(0)

            result.n_terms += 1

        return result

    @staticmethod
    def mmult(matrix_a: SparseMatrix, matrix_b: SparseMatrix) -> SparseMatrix:
        # Check if n_cols of A = n_rows of B
        if matrix_a.n_cols != matrix_b.n_rows:
            print('Incompatible matrices')
            raise SystemExit

        # Initialize the result matrix
        result = SparseMatrix(matrix_a.n_rows, matrix_b.n_cols, 0, [])

        # Set the required variables for matrix multiplication
        row = matrix_a.terms[0].row  # B의 열과 곱해질 A의 행
        row_begin = 0  # A 현재 행의 첫 번째 원소 위치
        matrix_b_transposed = matrix_b.fast_transpose()
        total_terms = 0  # 곱셈 결과 행렬의 현재 원소 수
        curr_sum = 0

        # Set the boundary conditions
        matrix_a.terms.append(Term(matrix_a.n_rows, None, None))
        matrix_b_transposed.terms.append(Term(matrix_b.n_cols, 0, None))

        i, j = 0, 0  # i는 A의, j는 B의 현재 항 인덱스
        while i < matrix_a.n_terms:
            column = matrix_b_transposed.terms[0].row  # A의 행과 곱해질 B의 열
            j = 0
            while j <= matrix_b.n_terms:
                # Multiply A's row with B's col

                # Current terms of A and B
                term_a = matrix_a.terms[i]
                term_b = matrix_b_transposed.terms[j]

                if term_a.row != row:
                    # row에 0이 아닌 항이 남지 않은 상태
                    # 결과 저장 후 curr_sum 재설정
                    total_terms, curr_sum = SparseMatrix.store_sum(
                        result, total_terms, row, column, curr_sum)

                    # A의 현재 행 첫 항으로 다시 돌아감
                    i = row_begin
                    # B 다음 열로 이동
                    while matrix_b_transposed.terms[j].row == column:
                        j += 1
                    column = matrix_b_transposed.terms[j].row
                elif term_b.row != column:
                    # column에 0이 아닌 항이 남지 않은 상태
                    # 결과 저장 후 curr_sum 재설정
                    total_terms, curr_sum = SparseMatrix.store_sum(
                        result, total_terms, row, column, curr_sum)

                    # A의 현재 행 첫 항으로 다시 돌아감
                    i = row_begin
                    # B 현재 열 변수 업데이트
                    column = term_b.row
                elif column == matrix_b.n_cols:
                    # A 현재 행의 곱 완료
                    # 결과 저장 후 curr_sum 재설정
                    total_terms, curr_sum = SparseMatrix.store_sum(
                        result, total_terms, row, column, curr_sum)

                    j += 1
                else:
                    # 현재 행 X 열에 곱할 항들이 남아있는 상태
                    if term_a.col < term_b.col:
                        # A의 다음 항으로 이동
                        i += 1
                    elif term_a.col > term_b.col:
                        # B의 다음 항으로 이동
                        j += 1
                    else:
                        # A의 항과 B의 항을 곱해서 더함
                        curr_sum += (term_a.value * term_b.value)

                        # A와 B의 다음 항으로 이동
                        i += 1
                        j += 1
            # while j < matrix_b.n_terms 문의 끝

            # A 현재 행의 곱 완료. 다음 행으로 이동
            while matrix_a.terms[i].row == row:
                i += 1
            row_begin = i
            row = matrix_a.terms[i].row
        # while i < matrix_a.n_terms 문의 끝

        # 행렬 곱셈 완료
        matrix_a.terms.pop()
        result.n_terms = total_terms
        return result

    @staticmethod
    def store_sum(result: SparseMatrix, total_terms: int, row: int, column: int, curr_sum: int) -> (int, int):
        # Store if curr_sum isn't 0
        if curr_sum:
            result.terms.append(Term(row, column, curr_sum))

            total_terms += 1
            curr_sum = 0

        return total_terms, curr_sum
