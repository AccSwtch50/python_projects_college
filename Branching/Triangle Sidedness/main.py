def main():
    sides_triangle = [0, 0, 0]
    for side in range(0,3):
        sides_triangle[side] = int(input(f"Enter side {side + 1}: "))
    
    triangle_shape = "scalene"
    for side in range(2, -1, -1):
        side_a = sides_triangle[side]
        side_b = sides_triangle[side - 1]
        if side_a == side_b:
            side_c = sides_triangle[side - 2]
            if side_c == side_b:
                triangle_shape = "equilateral"
            else:
                triangle_shape = "isosceles"
    
    print(f"The shape made by combining the sides makes {'an' if triangle_shape.startswith(('a', 'i', 'u', 'e', 'o')) else 'a'} {triangle_shape} triangle")

main()