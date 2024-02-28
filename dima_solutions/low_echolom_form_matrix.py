class gg_low_echolon_form_checker:

 
    def find_nonzero_row(matrix, pivot_row, col):
        nrows = matrix.shape[0]
        for row in range(pivot_row, nrows):
            if matrix[row, col] != 0:
                return row
        return None
    
    def swap_rows(matrix, row1, row2):
        matrix[[row1, row2]] = matrix[[row2, row1]]





class low_echolon_form_checker:

    def find_nonzero_row(matrix, pivot_row, col):
        nrows = matrix.shape[0]
        for row in range(pivot_row, nrows):
            if matrix[row, col] != 0:
                return row
        return None
    
    def swap_rows(matrix, row1, row2):
        matrix[[row1, row2]] = matrix[[row2, row1]]



