class MachineLearningFilter:
    import pandas as __pd
    import pickle as __pickle

    __data = __pd.read_csv('Data_with_CLASSES.csv')
    del __data['Unnamed: 0']

    with open('ML_MODELS.pickle', 'rb') as __f:
        __MODELS = __pickle.load(__f)

    @staticmethod
    def __choice(feature: dict) -> dict:
        order = []
        to_return = dict()
        tmp = []
        for idx in ['Price', 'Memory', 'Battery', 'Camera']:
            if len(feature[idx]) != 0:
                tmp.append(sum(feature[idx]) / len(feature[idx]))
                order.append(idx.lower())
            else:
                tmp.append(0)
                order.append(None)

        std_feature = MachineLearningFilter.__MODELS['scaler'].transform([tmp])

        for i in range(len(order)):
            model = std_feature[0][i]
            if order[i] is not None:
                model = MachineLearningFilter.__MODELS[order[i]].predict([[model]])
                to_return[order[i] + '_class'] = model[0]

        return to_return

    @staticmethod
    def find_smartphone(features: dict):
        features = MachineLearningFilter.__choice(features)
        # order = ['price_class', 'memory_class', 'battery_class', 'camera_class']
        new_data = MachineLearningFilter.__data
        for column in features.keys():
            new_data = new_data[new_data[column] == features[column]]

        new_data = new_data.sort_values(by=['rating'], ascending=False)
        new_data = new_data['smartphones'].head(3).to_list()
        return new_data

# test_feature = {
#     'Price': [45000],
#     'Camera': [50],
#     'Battery': [5000],
#     'Memory': [128]
# }


# s = MachineLearningFilter.find_smartphone(test_feature)
# print(s)
