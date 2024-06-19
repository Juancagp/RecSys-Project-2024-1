def get_metrics(model_name, predictions, ground_truth, path='./', k=20):
    mrr = 0
    recall = 0
    num_users = len(ground_truth)

    for user_idx in range(num_users):
        user_predictions = predictions[user_idx][:k]
        user_ground_truth = ground_truth[user_idx]

        # Calcula el MRR
        for rank, item in enumerate(user_predictions):
            if item in user_ground_truth:
                mrr += 1.0 / (rank + 1)
                break

        # Calcula el Recall
        relevant_items = len(set(user_predictions) & set(user_ground_truth))
        recall += relevant_items / len(user_ground_truth)

    mrr /= num_users
    recall /= num_users

    write_metrics_to_file(model_name, k, mrr, recall, f'{path}{model_name}.txt')

    return mrr, recall


def write_metrics_to_file(model_name, k, mrr, recall, file_path):
    with open(file_path, 'w') as file:
        file.write(f"Model: {model_name}\n")
        file.write(f"MRR@{k}: {mrr:.6f}\n")
        file.write(f"Recall@{k}: {recall:.6f}\n")
        file.write("\n")


