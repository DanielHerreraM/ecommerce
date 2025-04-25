import {configureStore, applyMiddleware, combineReducers} from 'redux';
import thunk from 'redux-thunk';
import categoriesReducers from '../reducers/categoriesReducers';
import productsReducer from '../reducers/productsReducers';

const rootReducer = combineReducers({
    catgories: categoriesReducers,
    products: productsReducer
});

const store = configureStore(rootReducer, applyMiddleware(thunk));

export default store;