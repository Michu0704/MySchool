import  React, { Component } from  'react';

import  MySchoolService  from  './MySchoolService';

const  myschoolService  =  new  MySchoolService();

class  CatalogsList  extends  Component {

    constructor(props) {
        super(props);
        this.state = {
            catalogs: [],
        };
    }

    componentDidMount() {
        var self = this;
        myschoolService.getCatalogs().then(function (result) {
            self.setState({catalogs: result.data})
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
            </div>
        );
    }
}

export  default  CatalogsList;