This is the Dressipi RecSys Challenge 2022 dataset. It contains training data of 1 million sessions and three different test sets, all from the same test month. The "leaderboard" and "final" test sets are the test sets of the RecSys challenge. As part of the challenge the sessions were randomly truncated to the first 50%-100% of their length. The "full" test set gives the complete test month's data without truncating the sessions.

The dataset is released under the following licence: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).


###############################################################################
# Training Data

train_purchases.csv
columns: session_id, item_id
The purchase that happened at the end of the session. One purchase per session.

train_sessions.csv
columns: session_id, item_id, date
The items that were viewed in a session. The "date" column is a timestamp to miliseconds. A session is equal to a day, so a session is one user's activity on one day. The session goes up to and not including the first time the user viewed the item that they bought in the end. The last item in the session will be the last item viewed before viewing the item that they bought. To find the item they bought link to train_purchases.csv on session_id.

item_features.csv
columns: item_id, feature_category_id, feature_value_id
The label data of items. A feature_category_id represents an aspect of the item such as "colour", the feature_value_id is the value for that aspect, e.g. "blue". Some items may not share many feature_cateogry_ids if they are different types of items, for example trousers will share almost nothing with shirts.

candidate_items.csv
columns: item_id
The candidate items to recommend from. This is the same list for all test sets.


###############################################################################
# Test Data: Full

test_full_sessions.csv
columns: session_id, item_id, date
The input sessions for prediction for the test month. These are the full sessions without truncation.

test_full_purchases.csv
columns: session_id, item_id
The correct purchase to be predicted for each session.


###############################################################################
# Test data: RecSys Challenge Leaderboard

test_leaderboard_sessions.csv
columns: session_id, item_id, date
The input sessions for prediction for the leaderboard. The sessions here were truncated as part of the RecSys Challenge task.

test_leaderboard_purchases.csv
columns: session_id, item_id
The correct purchase to be predicted for each session.


###############################################################################
# Test data: RecSys Challenge Final

test_final_sessions.csv
columns: session_id, item_id, date
The input sessions for prediction for determining the final winners. The sessions here were truncated as part of the RecSys Challenge task.

test_final_purchases.csv
columns: session_id, item_id
The correct purchase to be predicted for each session.

