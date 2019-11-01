import React from 'react'
import axios from 'axios'
import URL from './Global'
import BarraSuperior from './BarraSuperior'
import SlideProduto from './SlideProduto'
import ListaProduto from './ListaProduto'
import './css/w3.css'


class Home extends React.Component {
    constructor(props) {
        super(props);
        this.state = {description: '', 
                        items: [],
                        categories: [], 
                        cat_sel: ''}
        this.refresh = this.refresh.bind(this);
        this.handleAdd = this.handleAdd.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleRemove = this.handleRemove.bind(this);
        this.handleChangeCategory = this.handleChangeCategory.bind(this);

        const token = localStorage.getItem('@todo-app/token');
        this.config_axios = {
            headers: { Authorization: "Token " + token }
        };
               
        this.refresh(true);
    }

    refresh(first = false) {
        axios.get(URL, this.config_axios)
            .then(resp => this.setState({description: '', items: resp.data}));
        
        axios.get(URL + 'categories/', this.config_axios)
            .then(resp => this.setState({categories: resp.data, cat_sel: (first) ? resp.data[0].id : this.state.cat_sel}));
        
    }

    handleAdd() {
        axios.post(URL, { 'desc': this.state.description, 'category_id': this.state.cat_sel }, this.config_axios)
            .then(resp => this.refresh());
    }

    handleChange(e) {
        this.setState({description: e.target.value});
    }

    handleRemove(item) {        
        axios.delete(URL + item.id + '/', this.config_axios)
            .then(resp => this.refresh());
    }

    handleChangeCategory(e) {
        this.setState({cat_sel: e.target.value});        
    }

    render() {
        return (   
            <div>
                <BarraSuperior />
                <SlideProduto />
                <ListaProduto />
            </div>
        );
    }
}

export default Home;