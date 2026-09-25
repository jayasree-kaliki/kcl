# Python Program to Verify Kirchhoff's Current Law (KCL)
# Electrical Engineering - Network Analysis

print("==============================================")
print("       KIRCHHOFF'S CURRENT LAW (KCL)")
print("==============================================")

# Number of currents entering the node
n_entering = int(input("Enter number of currents entering the node: "))

sum_entering = 0

for i in range(n_entering):
    I = float(input(f"Enter entering current I{i + 1} (A): "))
    sum_entering += I

# Number of currents leaving the node
n_leaving = int(input("\nEnter number of currents leaving the node: "))

sum_leaving = 0

for i in range(n_leaving):
    I = float(input(f"Enter leaving current I{i + 1} (A): "))
    sum_leaving += I

# KCL difference
difference = sum_entering - sum_leaving

print("\n------------- RESULTS ----------------")
print(f"Total Current Entering = {sum_entering:.2f} A")
print(f"Total Current Leaving  = {sum_leaving:.2f} A")
print(f"Difference              = {difference:.4f} A")

# Verify KCL
print("\nKCL Verification:")

if abs(difference) < 0.000001:
    print("KCL is VERIFIED")
    print("Sum of currents entering = Sum of currents leaving")
else:
    print("KCL is NOT VERIFIED")

print("======================================")
