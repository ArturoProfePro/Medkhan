import CurrentPath from '../../../components/CurrentPath/ui/ui'
import Form from '../components/Form/ui/ui'
import StockList from '../components/StockList/ui/ui'
import c from './ui.module.scss'

const Stock = () => {

    return (
        <div className={c.container}>
            <CurrentPath />
            <StockList />
            <Form />
        </div>
    )
}

export default Stock