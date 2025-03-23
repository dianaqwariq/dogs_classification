
def calculates_results_stats(results):
    """
    Calculates statistics of the results of the program run using classifier's
    model architecture to classify the images.

    Parameters:
      results - Dictionary with key as image filename and value as a List
                [pet image label (string), classifier label (string), 
                 match (1/0) between pet image and classifier labels, 
                 1 if pet image 'is-a' dog, 0 if pet Image 'is-NOT-a' dog, 
                 1 if classifier classifies image 'as-a' dog, 
                 0 if classifier classifies image 'as-NOT-a' dog]

                        'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """
    # Replace None with the results_stats_dic dictionary that you created with
    # this function

    results_stats = {
        'n_images': len(results),
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0,
        'n_match': 0,
        'pct_match': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
        'pct_correct_notdogs': 0.0
    }

    for key in results:
        if results[key][2] == 1:
            results_stats['n_match'] += 1

        if results[key][3] == 1:
            results_stats['n_dogs_img'] += 1
            if results[key][2] == 1:
                results_stats['n_correct_breed'] += 1
            if results[key][4] == 1:
                results_stats['n_correct_dogs'] += 1
        else:
            results_stats['n_notdogs_img'] += 1
            if results[key][4] == 0:
                results_stats['n_correct_notdogs'] += 1

    # Calculate percentages
    if results_stats['n_images'] > 0:
        results_stats['pct_match'] = 100 * (results_stats['n_match'] /
                                            results_stats['n_images'])

    if results_stats['n_dogs_img'] > 0:
        results_stats['pct_correct_dogs'] = (results_stats['n_correct_dogs'] /
                                             results_stats['n_dogs_img']) * 100

        results_stats['pct_correct_breed'] = (results_stats['n_correct_breed']
                                              / results_stats['n_dogs_img'])*100

    if results_stats['n_notdogs_img'] > 0:
        results_stats['pct_correct_notdogs'] = (results_stats['n_correct_notdogs'] /
                                                results_stats['n_notdogs_img']) * 100.0

    return results_stats
