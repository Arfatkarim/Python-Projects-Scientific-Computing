def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    results_line = []

    for problem in problems:
        # Split each problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."

        operand1, operator, operand2 = parts

        # Check operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check operand length
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width for formatting
        width = max(len(operand1), len(operand2)) + 2  # 2 for operator and space

        # Format each line
        first_line.append(operand1.rjust(width))
        second_line.append(operator + ' ' + operand2.rjust(width - 2))
        dashes_line.append('-' * width)

        # Compute result if requested
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            results_line.append(result.rjust(width))

    # Join each line with four spaces in between
    arranged_first = '    '.join(first_line)
    arranged_second = '    '.join(second_line)
    arranged_dashes = '    '.join(dashes_line)
    arranged_result = '    '.join(results_line)

    if show_answers:
        return f"{arranged_first}\n{arranged_second}\n{arranged_dashes}\n{arranged_result}"
    else:
        return f"{arranged_first}\n{arranged_second}\n{arranged_dashes}"

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))