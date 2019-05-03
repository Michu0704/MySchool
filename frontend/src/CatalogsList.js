import  React, { Component } from  'react';

import  MySchoolService  from  './MySchoolService';

const  myschoolService  =  new  MySchoolService();

class  CatalogsList  extends  Component {

    constructor(props) {
        super(props);
        this.state = {
            catalogs: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
    }

    componentDidMount() {
        var self = this;
        myschoolService.getCatalogs().then(function (result) {
            self.setState({catalogs: result.data, nextPageURL: result.nextlink})
        });
    }

    nextPage() {
        var self = this;
        myschoolService.getCatalogssByURL(this.state.nextPageURL).then((result) => {
            self.setState({catalogs: result.data, nextPageURL: result.nextlink})
        });
    }

    render() {

        return (
            <div className="catalogs--list">
                <table className="table">
                    <thead key="thead">
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Limit</th>
                        <th>Provider</th>
                        <th>Level</th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.state.catalogs.map(c =>
                        <tr key={c.pk}>
                            <td>{c.pk}  </td>
                            <td>{c.name}</td>
                            <td>{c.limit}</td>
                            <td>{c.provider}</td>
                            <td>{c.level}</td>
                        </tr>)}
                    </tbody>
                </table>
                <button className="btn btn-primary" onClick={this.nextPage}>Next</button>
            </div>
        );
    }
}

export  default  CatalogsList;