import React from 'react'
import './css/w3.css'
import './css/gc.css'

class ListaProduto extends React.Component {
    constructor(props) {
        super(props);
        this.printCategories = this.printCategories.bind(this);
    }

    printCategories() {
        return this.props.categories.map(e => <option key={e.id} value={e.id}>{e.name}</option>);
    }

    render() {
        return (   
            <div role="slide_produto" >
                Lista de produtos
            </div>
        );
    }
}

export default ListaProduto;