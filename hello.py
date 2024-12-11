import hashlib


def main() -> None:
    transactions = ["tx1", "tx2", "tx3", "tx4"]
    merkle_root = build_merkle_tree(transactions)
    print(f"Merkle Root: {merkle_root}")


def hash_pair(a: str, b: str) -> int:
    return hashlib.sha256((a + b).encode()).hexdigest()


def build_merkle_tree(leaves: list[str]) -> str:
    if len(leaves) % 2 != 0:
        leaves.append(leaves[-1])  # Duplicate last leaf if odd number
    tree = [hashlib.sha256(leaf.encode()).hexdigest() for leaf in leaves]
    while len(tree) > 1:
        temp = []
        for i in range(0, len(tree), 2):
            temp.append(hash_pair(tree[i], tree[i + 1]))
        tree = temp
    return tree[0]


if __name__ == "__main__":
    main()
