import axios from 'axios'
import { serverurl } from '../../data'

const getStatus = async (id) => {
	try {
    let code = await axios.get(serverurl + `post/${id}`)
    return code.status
  } catch (err) {
    return err.response.status
  }
}	

export { getStatus }
