import axios from 'axios'
import { serverurl } from '../../data'

const getPostInfo = async (id) => {
	try {
    let post = await axios.get(serverurl + `post/${id}`)
    return post.data
  } catch (err) {
    return err.response.status
  }
}	

export { getPostInfo }
