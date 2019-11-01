import React from 'react'
import './css/w3.css'
import './css/gc.css'

class BarraSuperior extends React.Component {
    constructor(props) {
        super(props);
        this.printCategories = this.printCategories.bind(this);
    }

    printCategories() {
        return this.props.categories.map(e => <option key={e.id} value={e.id}>{e.name}</option>);
    }

    render() {
        return (   
            <div role="main_bar" >
                <input id="search" onChange={this.props.handleChange} 
                    className="w3-input w3-border w3-round w3-col l5 w3-margin-right" 
                    placeholder="Tem tuuuuudo! pode procurar :)" />
            </div>
        );
    }
}

export default BarraSuperior;